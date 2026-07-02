#!/usr/bin/env python3
"""Validate YSP lesson-data JSON files.

This validator checks lesson-data JSON before any generated lesson HTML is built
or published.

Usage:
    python3 scripts/validate_lesson_data.py lesson-data/ca-life/u1-l2.json
    python3 scripts/validate_lesson_data.py lesson-data/ca-life/u1-l2.json --pretty

Exit codes:
    0 = validation passed
    1 = file / JSON read error
    2 = validation failed
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL_FIELDS = [
    "meta",
    "categories",
    "core",
    "extended",
    "phrases",
    "dialogues",
    "speaking",
    "culture",
    "pronunciation",
    "previously_learned",
]

REQUIRED_META_FIELDS = [
    "course_id",
    "course_name",
    "course_folder",
    "unit",
    "lesson",
    "lesson_code",
    "title_en",
    "title_zh",
    "cefr",
    "html_path",
    "image_prefix",
    "status",
]

COURSE_COUNT_RULES = {
    ("canada-en", "A2"): {
        "categories": 5,
        "core": 25,
        "extended": 30,
        "phrases": 5,
        "dialogues": 5,
        "speaking": 5,
        "culture": 2,
        "pronunciation_words": 5,
    },
    ("canada-en", "B1"): {
        "categories": 5,
        "core": 30,
        "extended": 30,
        "phrases": 5,
        "dialogues": 5,
        "speaking": 5,
        "culture": 2,
        "pronunciation_words": 5,
    },
    ("travel-en", "A1"): {
        "categories": 5,
        "core": 15,
        "extended": 30,
        "phrases": 5,
        "dialogues": 5,
        "speaking": 5,
        "culture": 2,
        "pronunciation_words": 5,
    },
    ("biz-en", "B2"): {
        "categories": 5,
        "core": 40,
        "extended": 30,
        "phrases": 5,
        "dialogues": 5,
        "speaking": 5,
        "culture": 2,
        "pronunciation_words": 5,
    },
}

REQUIRED_CORE_FIELDS = ["en", "zh", "pr", "cat", "m1", "m2", "e1", "e2", "p1", "p2"]
REQUIRED_EXTENDED_FIELDS = ["en", "zh", "pr", "cat", "m", "ex"]
REQUIRED_PHRASE_FIELDS = ["en", "zh", "note", "t"]
REQUIRED_DIALOGUE_FIELDS = ["id", "title", "tz", "tag", "sit", "rA", "rB", "lines", "tp", "tn"]
REQUIRED_SPEAKING_FIELDS = ["t", "q", "h"]
REQUIRED_CULTURE_FIELDS = ["slot", "title", "tz", "photo", "notes", "qs"]
REQUIRED_PRONUNCIATION_FIELDS = ["focus", "fz", "words", "tip", "prac"]
REQUIRED_PRONUNCIATION_WORD_FIELDS = ["w", "ipa", "bad", "tip"]


def add_error(errors: list[str], path: str, message: str) -> None:
    errors.append(f"{path}: {message}")


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def require_fields(obj: dict[str, Any], fields: list[str], path: str, errors: list[str]) -> None:
    for field in fields:
        if field not in obj:
            add_error(errors, path, f"missing required field '{field}'")


def validate_list_items(items: Any, required_fields: list[str], path: str, errors: list[str]) -> None:
    if not isinstance(items, list):
        add_error(errors, path, "must be a list")
        return

    for index, item in enumerate(items):
        item_path = f"{path}[{index}]"
        if not isinstance(item, dict):
            add_error(errors, item_path, "must be an object")
            continue
        require_fields(item, required_fields, item_path, errors)


def validate_categories(data: dict[str, Any], errors: list[str]) -> None:
    categories = data.get("categories")
    if not isinstance(categories, list):
        add_error(errors, "categories", "must be a list")
        return
    for index, category in enumerate(categories):
        if not is_non_empty_string(category):
            add_error(errors, f"categories[{index}]", "must be a non-empty string")


def validate_dialogues(dialogues: Any, errors: list[str]) -> None:
    validate_list_items(dialogues, REQUIRED_DIALOGUE_FIELDS, "dialogues", errors)
    if not isinstance(dialogues, list):
        return

    for dialogue_index, dialogue in enumerate(dialogues):
        if not isinstance(dialogue, dict):
            continue
        lines = dialogue.get("lines")
        path = f"dialogues[{dialogue_index}].lines"
        if not isinstance(lines, list) or not lines:
            add_error(errors, path, "must be a non-empty list")
            continue
        for line_index, line in enumerate(lines):
            if not (
                isinstance(line, list)
                and len(line) == 2
                and line[0] in {"A", "B"}
                and is_non_empty_string(line[1])
            ):
                add_error(errors, f"{path}[{line_index}]", "must be [speaker, text] with speaker A or B")


def validate_pronunciation(pronunciation: Any, errors: list[str]) -> None:
    if not isinstance(pronunciation, dict):
        add_error(errors, "pronunciation", "must be an object")
        return
    require_fields(pronunciation, REQUIRED_PRONUNCIATION_FIELDS, "pronunciation", errors)
    validate_list_items(pronunciation.get("words"), REQUIRED_PRONUNCIATION_WORD_FIELDS, "pronunciation.words", errors)


def calculate_counts(data: dict[str, Any]) -> dict[str, int]:
    pronunciation = data.get("pronunciation", {})
    words = pronunciation.get("words", []) if isinstance(pronunciation, dict) else []
    return {
        "categories": len(data.get("categories", [])) if isinstance(data.get("categories"), list) else -1,
        "core": len(data.get("core", [])) if isinstance(data.get("core"), list) else -1,
        "extended": len(data.get("extended", [])) if isinstance(data.get("extended"), list) else -1,
        "phrases": len(data.get("phrases", [])) if isinstance(data.get("phrases"), list) else -1,
        "dialogues": len(data.get("dialogues", [])) if isinstance(data.get("dialogues"), list) else -1,
        "speaking": len(data.get("speaking", [])) if isinstance(data.get("speaking"), list) else -1,
        "culture": len(data.get("culture", [])) if isinstance(data.get("culture"), list) else -1,
        "pronunciation_words": len(words) if isinstance(words, list) else -1,
    }


def validate_counts(data: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    meta = data.get("meta", {})
    course_id = meta.get("course_id") if isinstance(meta, dict) else None
    cefr = meta.get("cefr") if isinstance(meta, dict) else None
    expected = COURSE_COUNT_RULES.get((course_id, cefr))
    actual = calculate_counts(data)

    if expected is None:
        add_error(errors, "meta", f"unsupported course_id / cefr combination: {course_id!r} / {cefr!r}")
        return {"expected": None, "actual": actual, "status": "failed"}

    for key, expected_value in expected.items():
        if actual.get(key) != expected_value:
            add_error(errors, key, f"expected {expected_value}, got {actual.get(key)}")

    return {"expected": expected, "actual": actual, "status": "passed" if not errors else "failed"}


def validate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []

    require_fields(data, REQUIRED_TOP_LEVEL_FIELDS, "root", errors)

    meta = data.get("meta")
    if not isinstance(meta, dict):
        add_error(errors, "meta", "must be an object")
    else:
        require_fields(meta, REQUIRED_META_FIELDS, "meta", errors)

    validate_categories(data, errors)
    validate_list_items(data.get("core"), REQUIRED_CORE_FIELDS, "core", errors)
    validate_list_items(data.get("extended"), REQUIRED_EXTENDED_FIELDS, "extended", errors)
    validate_list_items(data.get("phrases"), REQUIRED_PHRASE_FIELDS, "phrases", errors)
    validate_dialogues(data.get("dialogues"), errors)
    validate_list_items(data.get("speaking"), REQUIRED_SPEAKING_FIELDS, "speaking", errors)
    validate_list_items(data.get("culture"), REQUIRED_CULTURE_FIELDS, "culture", errors)
    validate_pronunciation(data.get("pronunciation"), errors)
    count_report = validate_counts(data, errors)

    return {"status": "passed" if not errors else "failed", "counts": count_report, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a YSP lesson-data JSON file.")
    parser.add_argument("json_file", help="Path to lesson-data JSON file")
    parser.add_argument("--pretty", action="store_true", help="Print a readable JSON validation report")
    args = parser.parse_args()

    path = Path(args.json_file)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 1

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON in {path}: {exc}", file=sys.stderr)
        return 1

    if not isinstance(data, dict):
        print(f"ERROR: root JSON value must be an object: {path}", file=sys.stderr)
        return 1

    report = validate(data)
    if args.pretty:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(report, ensure_ascii=False, separators=(",", ":")))

    return 0 if report["status"] == "passed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
