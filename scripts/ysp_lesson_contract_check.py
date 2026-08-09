# Run with: python3 scripts/ysp_lesson_contract_check.py
#
# Blocking validator for ChatGPT/Claude-generated YSP lesson pages.
# It validates v3.9 contract pages without blocking older legacy pages.
#
# v4 (2026-07-26): added two checks, both CRITICAL/blocking:
#   1. check_progress_accordion — Tab 10 Previously Learned must be a
#      collapsible accordion (.pvh/.pvb + toggle('open')), never a fully
#      expanded flat list. See Notion Skill Backup §10.2.
#   2. check_generic_filler — rejects canned template sentences such as
#      "A useful X word or expression for Y." / "Please help me with Y."
#      in Core/Extended meaning and example fields.
# These two checks were added following the Travel L04 ChatGPT-vs-Claude
# comparison (2026-07-26) and are documented in the Notion page
# "🔒 ChatGPT 課程產出強制執行合約" under 📋 ESL Skill Backup.

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS_ROOT = ROOT / "lessons"

ERRORS: list[tuple[str, str]] = []
WARNINGS: list[tuple[str, str]] = []

FORBIDDEN = [
    ".vocab-card",
    ".vocab-word",
    ".vocab-phonetic",
    ".vocab-meaning",
    ".vocab-chinese",
    ".vocab-example",
    ".vocab-grid",
    ".tab-container",
    ".tab-btn",
    ".tab-content",
    "vcard-front",
    "vcard-back",
    "vcard-en-front",
    "vcard-en-back",
]

SCRIPT_RE = re.compile(r"<script[\s\S]*?</script>", re.I)
LESSON_DATA_RE = re.compile(
    r"<script\b[^>]*\bid=[\"']lesson-data[\"'][^>]*>(?P<body>[\s\S]*?)</script>",
    re.I,
)

# v4 addendum (2026-07-26): generic template-filler sentence detection.
# These patterns are the exact "canned sentence" shapes found in rejected
# ChatGPT output (e.g. Travel L04 draft) and must never appear in Core `m1/m2`,
# Extended `m`, or example `e1/e2/ex` fields.
GENERIC_FILLER_PATTERNS = [
    re.compile(r"A useful [^.\"]{0,40} word or expression for", re.I),
    re.compile(r"Please help me with\s+\S", re.I),
]

# v4 addendum (2026-07-26): Tab 10 Previously Learned must be a collapsible
# accordion (per Skill Backup §10.2), never a fully expanded flat list.
PROGRESS_ACCORDION_TOKENS = ["pvh", "pvb"]

GALLERY_RESPONSIVE_REQUIREMENTS = {
    ".ysp-image-gallery-mount": {
        "min-width": "0",
        "overflow": {"hidden", "clip"},
    },
    ".ysp-image-gallery-grid": {
        "display": "grid",
        "width": "100%",
        "grid-template-columns": {"minmax(0,1fr)", "minmax(0px,1fr)"},
    },
    ".ysp-image-gallery-grid img": {
        "width": "100%",
        "max-width": "100%",
        "height": "auto",
        "aspect-ratio": "16/9",
        "object-fit": "contain",
    },
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def err(path: Path, message: str) -> None:
    ERRORS.append((rel(path), message))


def warn(path: Path, message: str) -> None:
    WARNINGS.append((rel(path), message))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def strip_scripts(text: str) -> str:
    return SCRIPT_RE.sub("", text)


def css_declarations(text: str, selector: str) -> dict[str, str]:
    matches = re.findall(
        rf"{re.escape(selector)}\s*\{{(?P<body>[^}}]*)\}}",
        text,
        flags=re.I,
    )
    declarations: dict[str, str] = {}
    for body in matches:
        for item in body.split(";"):
            if ":" not in item:
                continue
            name, value = item.split(":", 1)
            declarations[name.strip().lower()] = re.sub(r"\s+", "", value).lower()
    return declarations


def check_responsive_gallery_images(path: Path, text: str) -> None:
    """Gallery images must scale inside the lesson content mount.

    Added after the Travel L02 publication exposed intrinsic-width 1920 px
    images overflowing the 960 px lesson panel.
    """
    if "ysp-image-gallery" not in strip_scripts(text):
        return

    for selector, requirements in GALLERY_RESPONSIVE_REQUIREMENTS.items():
        declarations = css_declarations(text, selector)
        for name, expected in requirements.items():
            actual = declarations.get(name)
            allowed = expected if isinstance(expected, set) else {expected}
            if actual not in allowed:
                err(
                    path,
                    f"responsive Gallery CSS missing or invalid: {selector} "
                    f"requires {name}={sorted(allowed)!r}; found {actual!r}",
                )


def changed_html_candidates() -> set[Path]:
    candidates: set[Path] = set()

    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        for line in result.stdout.splitlines():
            if len(line) < 4:
                continue
            raw = line[3:].strip()
            if " -> " in raw:
                raw = raw.split(" -> ", 1)[1].strip()
            path = ROOT / raw
            if path.suffix.lower() == ".html" and path.exists():
                candidates.add(path)
    except Exception:
        pass

    for path in LESSONS_ROOT.glob("*/*.html"):
        if not path.is_file():
            continue
        text = read(path)
        if "data-ysp-contract" in text or "lesson-data" in text:
            candidates.add(path)

    inbox = ROOT / "image-inbox"
    if inbox.exists():
        for path in inbox.glob("*.html"):
            candidates.add(path)

    return candidates


def count_js_array_items(text: str, name: str) -> int | None:
    m = re.search(rf"\b(?:const|let|var)\s+{re.escape(name)}\s*=", text)
    if not m:
        return None

    start = text.find("[", m.end())
    if start < 0:
        return None

    depth = 0
    in_str: str | None = None
    escape = False
    item_commas = 0
    saw_value = False

    i = start
    while i < len(text):
        ch = text[i]

        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == in_str:
                in_str = None
            i += 1
            continue

        if ch in ("'", '"', "`"):
            in_str = ch
            saw_value = True
        elif ch == "[":
            depth += 1
            if depth == 2:
                saw_value = True
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return item_commas + 1 if saw_value else 0
        elif ch == "," and depth == 1:
            item_commas += 1

        i += 1

    return None


def expected_core_count(course_id: str, cefr: str) -> int | None:
    cefr = (cefr or "").upper().replace(" ", "")
    if course_id == "travel-en":
        return 15
    if course_id == "biz-en":
        return 40
    if course_id == "canada-en":
        if "B1" in cefr and "A2" not in cefr:
            return 30
        return 25
    return None


def check_progress_accordion(path: Path, text: str) -> None:
    """v4 addendum (2026-07-26): Tab 10 Previously Learned must use the
    collapsible accordion pattern (`.pvh` header + `.pvb` body, toggled via
    `classList.toggle('open')`, JavaScript-string escaped
    `classList.toggle(\'open\')`, or `toggle(&#39;open&#39;)`), per Skill Backup §10.2.
    A fully expanded flat word list is a CRITICAL violation."""
    if "previously_learned" not in text and "PREV" not in text:
        # No Previously Learned data at all (e.g. a course's first lesson) —
        # nothing to check here.
        return

    has_tokens = all(f'"{tok}' in text or f"'{tok}" in text or tok in text for tok in PROGRESS_ACCORDION_TOKENS)
    # Generated lesson renderers build the accordion markup inside a
    # single-quoted JavaScript string, so the quotes around ``open`` are
    # escaped in the HTML source (``toggle(\'open\')``). At runtime this is
    # the same onclick handler as ``toggle('open')``. Accept both source
    # representations, double quotes, and the existing HTML-entity form.
    quote = r"(?:\\?['\"]|&#39;)"
    has_toggle = bool(re.search(rf"toggle\({quote}open{quote}\)", text))

    if not (has_tokens and has_toggle):
        err(
            path,
            "Tab 10 Previously Learned is not a collapsible accordion "
            "(missing .pvh/.pvb structure or toggle('open') interaction); "
            "a fully expanded flat word list is forbidden per §10.2",
        )


def check_generic_filler(path: Path, text: str) -> None:
    """v4 addendum (2026-07-26): reject canned template sentences such as
    'A useful hotel word or expression for X.' or 'Please help me with X.'
    in place of a real, situational definition/example sentence."""
    lesson_data = LESSON_DATA_RE.search(text)
    scope = lesson_data.group("body") if lesson_data else text

    for pattern in GENERIC_FILLER_PATTERNS:
        hits = pattern.findall(scope)
        if hits:
            err(
                path,
                f"generic template-filler sentence found ({len(hits)}x): "
                f"pattern '{pattern.pattern}' — meaning/example fields must "
                "be specific, situational sentences, not word-substituted templates",
            )


def check_common_html(path: Path, text: str) -> None:
    stripped = strip_scripts(text)

    for pattern in FORBIDDEN:
        if pattern in text:
            err(path, f"forbidden legacy pattern found: {pattern}")

    tb = len(re.findall(r"class=[\"'][^\"']*\btb\b", stripped))
    tpn = len(re.findall(r"class=[\"'][^\"']*\btpn\b", stripped))
    if tb != 10:
        err(path, f"tab button count is {tb}; expected exactly 10")
    if tpn != 10:
        err(path, f"tab panel count is {tpn}; expected exactly 10")

    for cls in [".vc", ".vf", ".vb", ".famb", ".fm"]:
        if cls not in text:
            err(path, f"L02 short class system missing: {cls}")

    # Gallery tabs must use stable content mounts.
    for n in range(4, 9):
        if re.search(rf"getElementById\([\"']t{n}[\"']\)\.innerHTML", text):
            err(path, f"renderer overwrites full gallery tab t{n}; use t{n}c content mount")

    for gallery_id in [
        "phrases",
        "pronunciation",
        "speaking",
        "culture",
    ]:
        if f"-{gallery_id}" not in stripped:
            err(path, f"missing raw gallery block for {gallery_id}")

    for i in range(1, 6):
        if f"-d{i:02d}" not in stripped:
            err(path, f"missing raw dialogue gallery block d{i:02d}")

    if "YSP_IMAGE_GALLERY_MOUNT_START" not in stripped or "YSP_IMAGE_GALLERY_MOUNT_END" not in stripped:
        err(path, "gallery mount markers are missing")

    check_responsive_gallery_images(path, text)

    # v4 addendum (2026-07-26): Progress Check accordion + generic filler checks.
    check_progress_accordion(path, text)
    check_generic_filler(path, text)


def validate_json_contract(path: Path, text: str, data: dict) -> None:
    meta = data.get("meta") or {}
    course_id = meta.get("course_id", "")
    cefr = meta.get("cefr", "")
    expected_core = expected_core_count(course_id, cefr)

    expected = {
        "categories": 5,
        "extended": 30,
        "phrases": 5,
        "dialogues": 5,
        "speaking": 5,
        "culture": 2,
    }

    if expected_core is not None:
        expected["core"] = expected_core

    for key, count in expected.items():
        actual = len(data.get(key) or [])
        if actual != count:
            err(path, f"{key} count is {actual}; expected exactly {count}")

    pron_words = (((data.get("pronunciation") or {}).get("words")) or [])
    if not (3 <= len(pron_words) <= 5):
        err(path, f"pronunciation words count is {len(pron_words)}; expected 3 to 5")

    for idx, item in enumerate(data.get("core") or [], start=1):
        for field in ["en", "zh", "pr", "cat", "m1", "m2", "e1", "e2", "p1", "p2", "svg"]:
            if field not in item or (field != "cat" and not item.get(field)):
                err(path, f"core item {idx} missing {field}")
        if item.get("svg") and 'viewBox="0 0 80 80"' not in item.get("svg"):
            err(path, f"core item {idx} SVG must use viewBox=\"0 0 80 80\"")

    for idx, d in enumerate(data.get("dialogues") or [], start=1):
        lines = d.get("lines") or []
        if len(lines) < 6:
            err(path, f"dialogue {idx} has {len(lines)} lines; expected at least 6")


def validate_js_contract(path: Path, text: str) -> None:
    counts = {
        "CATS": 5,
        "V": 25,
        "EXT": 30,
        "PHRASES": 5,
        "DIALOGUES": 5,
        "SPEAKING": 5,
        "CULTURE": 2,
    }

    for name, expected in counts.items():
        actual = count_js_array_items(text, name)
        if actual is None:
            err(path, f"missing data array: {name}")
        elif actual != expected:
            err(path, f"{name} count is {actual}; expected exactly {expected}")

    if "viewBox=\"0 0 80 80\"" not in text and "viewBox='0 0 80 80'" not in text:
        err(path, "Core SVG icon system must use viewBox=\"0 0 80 80\"")


def validate_file(path: Path) -> None:
    text = read(path)

    # Only enforce on generated / contract-aware pages.
    if "data-ysp-contract" not in text and "lesson-data" not in text:
        return

    check_common_html(path, text)

    lesson_data = LESSON_DATA_RE.search(text)
    if lesson_data:
        body = lesson_data.group("body").strip()
        # The fixed HTML template intentionally contains the exact data
        # placeholder. Its structure is checked above; generated pages still
        # have their embedded lesson JSON parsed and validated below.
        if body == "{{LESSON_DATA_JSON}}":
            return
        try:
            data = json.loads(body)
        except json.JSONDecodeError as exc:
            err(path, f"lesson-data JSON is invalid: {exc}")
            return
        validate_json_contract(path, text, data)
    else:
        validate_js_contract(path, text)


def main() -> None:
    candidates = sorted(changed_html_candidates())

    print("=" * 60)
    print("YSP Lesson Content Contract Check")
    print("=" * 60)

    checked = 0
    for path in candidates:
        if not path.exists():
            continue
        text = read(path)
        if "data-ysp-contract" not in text and "lesson-data" not in text:
            continue
        checked += 1
        validate_file(path)

    print(f"Files checked : {checked}")
    print(f"Errors        : {len(ERRORS)}")
    print(f"Warnings      : {len(WARNINGS)}")
    print()

    if ERRORS:
        print("ERRORS")
        print("------")
        for file_name, message in ERRORS:
            print(f"  {file_name}")
            print(f"    ✗ {message}")
        print()

    if WARNINGS:
        print("WARNINGS")
        print("--------")
        for file_name, message in WARNINGS:
            print(f"  {file_name}")
            print(f"    ⚠ {message}")
        print()

    if not ERRORS and not WARNINGS:
        print("All lesson content contract checks passed.")

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
