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


def validate(path: Path) -> None:
    text = read(path)
    if "data-ysp-contract" not in text and "lesson-data" not in text:
        return

    if "Drilling Practice｜句型替換練習" not in text:
        err(path, "missing Drilling Practice tab/content")

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

    if not re.search(r"classList\.toggle\([\"']sa[\"']\)", text):
        err(path, "drilling card does not reveal the answer by flip/toggle interaction")

    if not contains_any(text, ["上一個", "Previous"]):
        err(path, "drilling navigation is missing the previous button")
    if not contains_any(text, ["下一個", "Next"]):
        err(path, "drilling navigation is missing the next button")
    if "V.length" not in text:
        err(path, "drilling does not iterate through the complete Core vocabulary set")

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
