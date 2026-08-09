# Run with: python3 scripts/ysp_drilling_contract_check.py
#
# Blocking validator for the Golden L02 three-mode Drilling Practice system.
# It checks contract-aware lessons without changing lesson content.

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS_ROOT = ROOT / "lessons"

ERRORS: list[tuple[str, str]] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def err(path: Path, message: str) -> None:
    ERRORS.append((rel(path), message))


def candidates() -> set[Path]:
    result: set[Path] = set()

    try:
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        for line in status.stdout.splitlines():
            if len(line) < 4:
                continue
            raw = line[3:].strip()
            if " -> " in raw:
                raw = raw.split(" -> ", 1)[1].strip()
            path = ROOT / raw
            if path.suffix.lower() == ".html" and path.exists():
                result.add(path)
    except Exception:
        pass

    for path in LESSONS_ROOT.glob("*/*.html"):
        if not path.is_file():
            continue
        text = read(path)
        if "data-ysp-contract" in text or "lesson-data" in text:
            result.add(path)

    inbox = ROOT / "image-inbox"
    if inbox.exists():
        result.update(path for path in inbox.glob("*.html") if path.is_file())

    return result


def contains_any(text: str, values: list[str]) -> bool:
    return any(value in text for value in values)


def function_scope(text: str, start_name: str, end_name: str) -> str:
    """Return the source region spanning adjacent minified render helpers."""
    start = text.find(f"function {start_name}")
    if start < 0:
        return ""
    end = text.find(f"function {end_name}", start + 1)
    return text[start:] if end < 0 else text[start:end]


def drilling_scope(text: str) -> str:
    """Return helpers and renderer that implement Drilling, excluding other tabs."""
    starts = [
        text.find(f"function {name}")
        for name in ["ffLabel", "toggleDF", "drillIds", "r3"]
    ]
    starts = [position for position in starts if position >= 0]
    if not starts:
        return ""
    start = min(starts)
    end = text.find("function r4", start + 1)
    return text[start:] if end < 0 else text[start:end]


def validate(path: Path) -> None:
    text = read(path)
    if "data-ysp-contract" not in text and "lesson-data" not in text:
        return

    if not contains_any(text, ["🔁 Drilling", "Drilling Practice｜句型替換練習"]):
        err(path, "missing Drilling tab/content")

    # Labels may use the older Golden L02 wording "L1 跟唸" or the clearer
    # production wording "L1 單字跟唸". The behavior requirements below are strict.
    if not contains_any(text, ["L1 單字跟唸", "L1 跟唸"]):
        err(path, "missing L1 word-repeat mode")
    if not contains_any(text, ["L2 整句跟唸", "L2 整句", "L2 Sentence Repeat"]):
        err(path, "missing L2 full-sentence-repeat mode")
    if not contains_any(text, ["L3 中翻英", "L3 Chinese-to-English"]):
        err(path, "missing L3 Chinese-to-English mode")

    required_css = [".dzone", ".dc", ".dc.sa .da", ".dn", ".dbtn", ".lt", ".lb"]
    for token in required_css:
        if token not in text:
            err(path, f"missing drilling flip-card CSS token: {token}")

    # Drilling markup is generated inside a JavaScript string, where the
    # quotes around ``sa`` are escaped in the HTML source. The runtime
    # handler is equivalent to an unescaped ``classList.toggle('sa')``.
    quote = r"\\?['\"]"
    if not re.search(rf"classList\.toggle\({quote}sa{quote}\)", text):
        err(path, "drilling card does not reveal the answer by flip/toggle interaction")

    if not contains_any(text, ["上一個", "Previous"]):
        err(path, "drilling navigation is missing the previous button")
    if not contains_any(text, ["下一個", "Next"]):
        err(path, "drilling navigation is missing the next button")
    if "V.length" not in text:
        err(path, "drilling does not iterate through the complete Core vocabulary set")

    drilling = drilling_scope(text)
    if not drilling:
        err(path, "cannot locate the Drilling renderer/helper source")
    else:
        # Current final rule: Drilling filters are familiarity-only and cover
        # unassessed plus all three assessed states. Each state is independently
        # toggled so the filter remains multi-select.
        golden_filter = all(
            token in drilling
            for token in ["ffLabel", "[0,1,2,3]", "toggleFF", "ff[k]=!ff[k]"]
        )
        set_filter = bool(
            re.search(r"new\s+Set\(\)", text)
            and re.search(r"function\s+toggleDF\b", drilling)
            and all(f"toggleDF({state}" in drilling for state in [0, 1, 2, 3])
            and re.search(r"\.has\(l\)\?.*\.delete\(l\):.*\.add\(l\)", drilling)
        )
        if not (golden_filter or set_filter):
            err(path, "drilling lacks a multi-select familiarity-only filter for states 0/1/2/3")

        full_core_pool = bool(
            re.search(r"V\.map\(\(v,i\)=>\(\{v:v,i:i\}\)\)", drilling)
            or re.search(r"Array\.from\(\{length:V\.length\}", drilling)
        )
        if not full_core_pool:
            err(path, "drilling familiarity pool does not begin with the complete Core vocabulary set")
        familiarity_filter = bool(
            re.search(r"\.filter\(x=>ff\[fam\[x\.i\]\|\|0\]\)", drilling)
            or re.search(r"\.filter\(i=>!dFilters\.size\|\|dFilters\.has\(fam\[i\]\|\|0\)\)", drilling)
        )
        if not familiarity_filter:
            err(path, "drilling pool is not filtered exclusively by familiarity state")

        forbidden_filter_patterns = [
            (r"\bCATS\b", "category list"),
            (r"\.cat\b", "category field"),
            (r"data-(?:cat|topic)\b", "category/topic data attribute"),
            (r"\b(?:category|topic)Filter\b", "category/topic filter helper"),
        ]
        for pattern, description in forbidden_filter_patterns:
            if re.search(pattern, drilling, re.I):
                err(path, f"forbidden Drilling category/topic filtering found: {description}")

    familiarity = function_scope(text, "sf", "us")
    toggle_off = bool(
        re.search(r"fam\[i\]\s*===\s*l", familiarity)
        and (
            re.search(r"delete\s+fam\[i\]", familiarity)
            or re.search(r"fam\[i\]\s*=\s*fam\[i\]\s*===\s*l\s*\?\s*0\s*:\s*l", familiarity)
        )
    )
    if not toggle_off:
        err(path, "familiarity marking does not toggle the selected state off to unassessed")

    # Required field use for the three modes.
    for token, description in [
        ("v.en", "Core English word"),
        ("v.pr", "Core pronunciation"),
        ("v.e1", "Core full example sentence"),
        ("v.zh", "Core Traditional Chinese meaning"),
    ]:
        if token not in text:
            err(path, f"drilling mode does not use required field: {description}")

    # Block the shallow static pattern-and-answer grid that caused the Travel L02 issue.
    static_markers = [
        "Pattern ${i+1}",
        "V.slice(0,10)",
        "Answer: ${esc(v.en)}",
    ]
    if all(marker in text for marker in static_markers):
        err(path, "static pattern/answer grid found; use the three-mode interactive flip-card drill")


def main() -> None:
    checked = 0
    print("=" * 64)
    print("YSP Drilling Practice Contract Check")
    print("=" * 64)

    for path in sorted(candidates()):
        text = read(path)
        if "data-ysp-contract" not in text and "lesson-data" not in text:
            continue
        checked += 1
        validate(path)

    print(f"Files checked : {checked}")
    print(f"Errors        : {len(ERRORS)}")
    print()

    if ERRORS:
        print("ERRORS")
        print("------")
        for file_name, message in ERRORS:
            print(f"  {file_name}")
            print(f"    ✗ {message}")
    else:
        print("All three-mode Drilling Practice contract checks passed.")

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
