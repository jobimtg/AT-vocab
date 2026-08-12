#!/usr/bin/env python3
"""Extract YSP Golden L02 lesson data from a v3.7 HTML file.

This script converts the JavaScript data arrays inside the Golden L02 HTML into
structured lesson-data JSON.

Usage:
    python3 scripts/extract_l02_source_data.py \
      --input L02_transportation_fixed_teacher_notes.html \
      --output lesson-data/ca-life/u1-l2.json

Why Node is used:
    The Golden L02 source stores arrays as JavaScript object literals, not strict
    JSON. Node's built-in VM can safely evaluate the extracted data block without
    adding Python dependencies.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REQUIRED_COUNTS = {
    "categories": 5,
    "core": 25,
    "extended": 30,
    "phrases": 5,
    "dialogues": 5,
    "speaking": 5,
    "culture": 2,
    "pronunciation_words": 5,
}

DATA_KEYS = ["CATS", "V", "EXT", "PHRASES", "DIALOGUES", "SPEAKING", "CULTURE", "PRON"]


def extract_data_script(html: str) -> str:
    position = 0
    while True:
        tag = html.find("<script", position)
        if tag == -1:
            break
        start = html.find(">", tag)
        if start == -1:
            break
        start += 1
        end = html.find("</script>", start)
        if end == -1:
            break
        script = html[start:end].strip()
        if any(marker in script for marker in ("var CATS", "const CATS")) and any(
            marker in script for marker in ("var V", "const V")
        ):
            return script
        position = end + len("</script>")
    raise ValueError("No script block contains the expected lesson data variables.")


def evaluate_js_data(script: str) -> dict:
    # The legacy source may keep renderer code after the data declarations.
    # It is neither required nor safe to execute that browser-only section.
    browser_marker = script.find("document.addEventListener")
    if browser_marker != -1:
        script = script[:browser_marker]
    node_code = f"""
const vm = require('vm');
const ctx = {{}};
vm.createContext(ctx);
vm.runInContext({json.dumps(script + ';globalThis.__YSP_DATA__ = {' + ','.join(DATA_KEYS) + '};')}, ctx);
const out = ctx.__YSP_DATA__;
console.log(JSON.stringify(out));
"""

    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tmp:
        tmp.write(node_code)
        tmp_path = Path(tmp.name)

    try:
        result = subprocess.run(
            ["node", str(tmp_path)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except FileNotFoundError as exc:
        raise RuntimeError("Node.js is required for extraction but was not found on PATH.") from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"Node extraction failed:\n{exc.stderr}") from exc
    finally:
        tmp_path.unlink(missing_ok=True)

    return json.loads(result.stdout)


def build_lesson_json(data: dict, source_file: str, meta: dict) -> dict:
    def pick(value: dict, *names: str, default=""):
        for name in names:
            if name in value:
                return value[name]
        return default

    core = [{
        "en": item["en"], "zh": item["zh"], "pr": pick(item, "pr", "pron"), "cat": item["cat"],
        "m1": pick(item, "m1", "meaning1"), "m2": pick(item, "m2", "meaning2"),
        "e1": pick(item, "e1", "ex1"), "e2": pick(item, "e2", "ex2"),
        "p1": pick(item, "p1", "pr1"), "p2": pick(item, "p2", "pr2"),
        **({"svg": item["svg"]} if "svg" in item else {}),
    } for item in data["V"]]
    extended = [{
        "en": item["en"], "zh": item["zh"], "pr": pick(item, "pr", "pron"),
        "cat": item["cat"], "m": pick(item, "m", "meaning"), "ex": pick(item, "ex"),
    } for item in data["EXT"]]
    phrases = [{"en": item["en"], "zh": item["zh"], "note": item["note"], "t": pick(item, "t", "tier")} for item in data["PHRASES"]]
    dialogues = [{
        "id": item["id"], "title": item["title"], "tz": pick(item, "tz", "titleZh"),
        "tag": item["tag"], "sit": pick(item, "sit", "situationA"),
        "rA": pick(item, "rA", "roleA"), "rB": pick(item, "rB", "roleB"),
        "lines": item["lines"], "tp": pick(item, "tp", "tryPrompt"), "tn": pick(item, "tn", "teacherNotes"),
    } for item in data["DIALOGUES"]]
    speaking = [{"t": pick(item, "t", "tier"), "q": item["q"], "h": pick(item, "h", "hint")} for item in data["SPEAKING"]]
    culture = [{
        "slot": item["slot"], "title": item["title"], "tz": pick(item, "tz", "titleZh"),
        "photo": item["photo"], "notes": item["notes"], "qs": pick(item, "qs", "questions", default=[]),
    } for item in data["CULTURE"]]
    raw_pron = data["PRON"]
    pron = {
        "focus": raw_pron["focus"], "fz": pick(raw_pron, "fz", "focusZh"),
        "words": [{"w": pick(word, "w", "word"), "ipa": word["ipa"], "bad": pick(word, "bad", "wrong"), "tip": word["tip"]} for word in raw_pron["words"]],
        "tip": raw_pron["tip"], "prac": pick(raw_pron, "prac", "practice"),
    }
    lesson = {
        "meta": {**meta, "source_file": source_file},
        "categories": data["CATS"],
        "core": core,
        "extended": extended,
        "phrases": phrases,
        "dialogues": dialogues,
        "speaking": speaking,
        "culture": culture,
        "pronunciation": pron,
        "previously_learned": {
            "source": "L01 required before cumulative tracking is finalized",
            "items": [],
        },
    }

    actual = {
        "categories": len(lesson["categories"]),
        "core": len(lesson["core"]),
        "extended": len(lesson["extended"]),
        "phrases": len(lesson["phrases"]),
        "dialogues": len(lesson["dialogues"]),
        "speaking": len(lesson["speaking"]),
        "culture": len(lesson["culture"]),
        "pronunciation_words": len(pron.get("words", [])),
    }

    failed = [key for key, expected in REQUIRED_COUNTS.items() if actual.get(key) != expected]
    lesson["validation"] = {
        "expected": REQUIRED_COUNTS,
        "actual": actual,
        "status": "passed" if not failed else "failed",
        "failed_checks": failed,
    }
    return lesson


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract Golden L02 source-data JSON from HTML.")
    parser.add_argument("--input", required=True, help="Path to Golden L02 HTML file")
    parser.add_argument("--output", required=True, help="Path to output lesson-data JSON")
    parser.add_argument("--unit", type=int, default=1)
    parser.add_argument("--lesson", type=int, default=2)
    parser.add_argument("--title-en", default="Transportation in Canada")
    parser.add_argument("--title-zh", default="加拿大交通")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
        return 1

    html = input_path.read_text(encoding="utf-8")
    script = extract_data_script(html)
    data = evaluate_js_data(script)
    lesson = build_lesson_json(data, input_path.name, {
        "course_id": "canada-en",
        "course_name": "Canada Life & Career English",
        "course_folder": "ca-life",
        "unit": args.unit,
        "lesson": args.lesson,
        "lesson_code": f"L{args.lesson:02d}",
        "title_en": args.title_en,
        "title_zh": args.title_zh,
        "cefr": "A2",
        "html_path": f"lessons/ca-life/u{args.unit}-l{args.lesson}.html",
        "image_prefix": f"l{args.lesson:02d}",
        "status": "approved-source",
    })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {output_path}")
    print(json.dumps(lesson["validation"], ensure_ascii=False, indent=2))

    return 0 if lesson["validation"]["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
