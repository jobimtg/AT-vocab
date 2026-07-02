# YSP Phase 5 Manual Step For User

_Last updated: 2026-07-02_

## Current Situation

The user does not need to manually write JSON or edit HTML.

However, because the raw Golden L02 HTML must not be committed to the public repository and the current GitHub connector cannot attach a local generated JSON file directly, there is one small manual bridge step.

## The One Manual Step

Use local Codex or a local repo environment to run the already-created extractor and validator.

## Exact Commands

Run from repo root after placing the Golden L02 source file locally:

```bash
python3 scripts/extract_l02_source_data.py \
  --input L02_transportation_fixed_teacher_notes.html \
  --output lesson-data/ca-life/u1-l2.json

python3 scripts/validate_lesson_data.py lesson-data/ca-life/u1-l2.json --pretty
```

## Expected Output

Validation should show:

```text
status: passed
categories: 5
core: 25
extended: 30
phrases: 5
dialogues: 5
speaking: 5
culture: 2
pronunciation_words: 5
```

## Commit Only This File

```text
lesson-data/ca-life/u1-l2.json
```

## Do Not Commit This File

```text
L02_transportation_fixed_teacher_notes.html
```

## Do Not Change These Files

```text
index.html
lessons/**/*.html
.github/workflows/**
scripts/ysp_site_maintenance.py
scripts/ysp_validate_site.py
lessons/index.html
assets/**
```

## Suggested Commit Message

```text
data: add validated L02 source-data JSON
```

## Suggested PR Title

```text
data: add validated L02 source-data JSON
```

## After This Step

Once the JSON is committed and validated, ChatGPT can continue automatically with:

```text
Phase 5.3 — Store fixed L02 template / renderer
Phase 5.4 — Create HTML builder
Phase 5.5 — Generate proof HTML in safe draft path
```
