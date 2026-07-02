#!/usr/bin/env python3
"""Build generated YSP lesson HTML from lesson-data JSON and the fixed L02 template.

Phase 5.4 purpose:
    Convert one validated lesson-data JSON file into one generated HTML file.

This script is intentionally conservative:
    - It validates lesson data before building.
    - It requires an explicit output path.
    - It refuses to write public lesson HTML under lessons/ unless --allow-public-output is passed.
    - It refuses to overwrite existing files unless --force is passed.

Recommended safe proof command for Phase 5.5:
    python3 scripts/build_lesson_html.py \
      --input lesson-data/ca-life/u1-l2.json \
      --template templates/lesson-l02-template.html \
      --output build/generated/ca-life-u1-l2.html

Public output command, only after review approval:
    python3 scripts/build_lesson_html.py \
      --input lesson-data/ca-life/u1-l2.json \
      --template templates/lesson-l02-template.html \
      --output lessons/ca-life/u1-l2.html \
      --allow-public-output
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

PLACEHOLDERS = [
    "TITLE_EN",
    "TITLE_ZH",
    "COURSE_ID",
    "COURSE_NAME",
    "LESSON_CODE",
    "LESSON_DESCRIPTION",
    "CEFR",
    "CORE_COUNT",
    "EXTENDED_COUNT",
    "DIALOGUE_COUNT",
    "ROOT_PREFIX",
    "LESSON_DATA_JSON",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RuntimeError(f"Input JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise RuntimeError(f"Root JSON value must be an object: {path}")
    return data


def run_validator(input_path: Path) -> None:
    root = repo_root()
    validator = root / "scripts" / "validate_lesson_data.py"
    if not validator.exists():
        raise RuntimeError(f"Validator not found: {validator}")

    result = subprocess.run(
        [sys.executable, str(validator), str(input_path), "--pretty"],
        cwd=root,
        text=True,
        capture_output=True,
        encoding="utf-8",
    )

    if result.returncode != 0:
        message = result.stdout.strip() or result.stderr.strip()
        raise RuntimeError(f"Lesson data validation failed:\n{message}")


def read_template(template_path: Path) -> str:
    try:
        template = template_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"Template file not found: {template_path}") from exc

    missing = [name for name in PLACEHOLDERS if "{{" + name + "}}" not in template]
    if missing:
        raise RuntimeError("Template is missing required placeholders: " + ", ".join(missing))
    return template


def root_prefix_for_output(output_path: Path) -> str:
    root = repo_root()
    output_abs = output_path.resolve()
    try:
        relative_parent = output_abs.parent.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f"Output path must be inside the repository: {output_path}") from exc

    depth = len(relative_parent.parts)
    return "" if depth == 0 else "../" * depth


def lesson_description(data: dict[str, Any]) -> str:
    meta = data.get("meta", {})
    title_en = meta.get("title_en", "this lesson") if isinstance(meta, dict) else "this lesson"
    course_name = meta.get("course_name", "YSP Learn & Shine") if isinstance(meta, dict) else "YSP Learn & Shine"
    return f"Practice practical English for {title_en} in {course_name}."


def build_replacements(data: dict[str, Any], output_path: Path) -> dict[str, str]:
    meta = data.get("meta", {})
    if not isinstance(meta, dict):
        raise RuntimeError("meta must be an object")

    replacements = {
        "TITLE_EN": str(meta.get("title_en", "")),
        "TITLE_ZH": str(meta.get("title_zh", "")),
        "COURSE_ID": str(meta.get("course_id", "")),
        "COURSE_NAME": str(meta.get("course_name", "")),
        "LESSON_CODE": str(meta.get("lesson_code", "")),
        "LESSON_DESCRIPTION": lesson_description(data),
        "CEFR": str(meta.get("cefr", "")),
        "CORE_COUNT": str(len(data.get("core", [])) if isinstance(data.get("core"), list) else 0),
        "EXTENDED_COUNT": str(len(data.get("extended", [])) if isinstance(data.get("extended"), list) else 0),
        "DIALOGUE_COUNT": str(len(data.get("dialogues", [])) if isinstance(data.get("dialogues"), list) else 0),
        "ROOT_PREFIX": root_prefix_for_output(output_path),
        "LESSON_DATA_JSON": json.dumps(data, ensure_ascii=False, indent=2),
    }
    return replacements


def render(template: str, replacements: dict[str, str]) -> str:
    html = template
    for key, value in replacements.items():
        html = html.replace("{{" + key + "}}", value)

    unresolved = [part.split("}}", 1)[0] for part in html.split("{{")[1:] if "}}" in part]
    if unresolved:
        raise RuntimeError("Generated HTML still contains unresolved placeholders: " + ", ".join(sorted(set(unresolved))))
    return html


def is_public_lesson_output(path: Path) -> bool:
    root = repo_root()
    try:
        relative = path.resolve().relative_to(root)
    except ValueError:
        return False
    return bool(relative.parts) and relative.parts[0] == "lessons" and relative.suffix.lower() == ".html"


def write_output(output_path: Path, html: str, *, force: bool, allow_public_output: bool) -> None:
    if is_public_lesson_output(output_path) and not allow_public_output:
        raise RuntimeError(
            "Refusing to write public lesson HTML under lessons/. "
            "Use --allow-public-output only after review approval."
        )

    if output_path.exists() and not force:
        raise RuntimeError(f"Output file already exists. Use --force to overwrite: {output_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build one YSP lesson HTML file from lesson-data JSON and template.")
    parser.add_argument("--input", required=True, help="Path to lesson-data JSON file")
    parser.add_argument("--template", default="templates/lesson-l02-template.html", help="Path to fixed lesson template")
    parser.add_argument("--output", required=True, help="Output HTML path")
    parser.add_argument("--force", action="store_true", help="Overwrite output file if it already exists")
    parser.add_argument(
        "--allow-public-output",
        action="store_true",
        help="Allow writing public HTML under lessons/. Use only after review approval.",
    )
    args = parser.parse_args()

    root = repo_root()
    input_path = (root / args.input).resolve() if not Path(args.input).is_absolute() else Path(args.input).resolve()
    template_path = (root / args.template).resolve() if not Path(args.template).is_absolute() else Path(args.template).resolve()
    output_path = (root / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output).resolve()

    try:
        run_validator(input_path)
        data = load_json(input_path)
        template = read_template(template_path)
        replacements = build_replacements(data, output_path)
        html = render(template, replacements)
        write_output(output_path, html, force=args.force, allow_public_output=args.allow_public_output)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {output_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
