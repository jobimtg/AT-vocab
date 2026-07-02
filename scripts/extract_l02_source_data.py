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


def extract_first_script(html: str) -> str:
    start = html.find("<script>")
    if start == -1:
        raise ValueError("No <script> block found in input HTML.")
    start += len("<script>")
    end = html.find("</script>", start)
    if end == -1:
        raise ValueError("No closing </script> found for first script block.")
    script = html[start:end].strip()
    if "var CATS" not in script or "var V" not in script:
        raise ValueError("First script block does not contain expected L02 data variables.")
    return script


def evaluate_js_data(script: str) -> dict:
    node_code = f"""
const vm = require('vm');
const ctx = {{}};
vm.createContext(ctx);
vm.runInContext({json.dumps(script)}, ctx);
const out = {{}};
for (const key of {json.dumps(DATA_KEYS)}) {{
  if (!(key in ctx)) {{
    throw new Error(`Missing variable ${{key}}`);
  }}
  out[key] = ctx[key];
}}
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


def build_lesson_json(data: dict, source_file: str) -> dict:
    pron = data["PRON"]
    lesson = {
        "meta": {
            "course_id": "canada-en",
            "course_name": "Canada Life & Career English",
            "course_folder": "ca-life",
            "unit": 1,
            "lesson": 2,
            "lesson_code": "L02",
            "title_en": "Transportation in Canada",
            "title_zh": "加拿大交通",
            "cefr": "A2",
            "html_path": "lessons/ca-life/u1-l2.html",
            "image_prefix": "l02",
            "status": "golden-reference",
            "source_file": source_file,
        },
        "categories": data["CATS"],
        "core": data["V"],
        "extended": data["EXT"],
        "phrases": data["PHRASES"],
        "dialogues": data["DIALOGUES"],
        "speaking": data["SPEAKING"],
        "culture": data["CULTURE"],
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
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
        return 1

    html = input_path.read_text(encoding="utf-8")
    script = extract_first_script(html)
    data = evaluate_js_data(script)
    lesson = build_lesson_json(data, input_path.name)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {output_path}")
    print(json.dumps(lesson["validation"], ensure_ascii=False, indent=2))

    return 0 if lesson["validation"]["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
