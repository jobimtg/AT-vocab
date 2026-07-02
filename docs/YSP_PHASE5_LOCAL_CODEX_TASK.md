# YSP Phase 5 Local Codex Task

_Last updated: 2026-07-02_

## Purpose

This file gives Codex or another local repo agent the exact safe task needed to finish Phase 5.1C.

The user confirmed that the raw Golden L02 HTML must not be committed to the public repo.

## Task

Generate and commit the full L02 source-data JSON from the local Golden L02 HTML file.

## Do Not Commit

```text
L02_transportation_fixed_teacher_notes.html
```

## Required Local Source File

The local file should exist outside the public repo or in an ignored local-only location:

```text
L02_transportation_fixed_teacher_notes.html
```

## Commands

Run from repo root:

```bash
python3 scripts/extract_l02_source_data.py \
  --input L02_transportation_fixed_teacher_notes.html \
  --output lesson-data/ca-life/u1-l2.json

python3 scripts/validate_lesson_data.py lesson-data/ca-life/u1-l2.json --pretty
```

## Expected Validation Result

```text
categories: 5
core: 25
extended: 30
phrases: 5
dialogues: 5
speaking: 5
culture: 2
pronunciation_words: 5
status: passed
```

## Files Allowed To Change

```text
lesson-data/ca-life/u1-l2.json
```

## Files Not Allowed To Change

```text
index.html
lessons/**/*.html
.github/workflows/**
scripts/ysp_site_maintenance.py
scripts/ysp_validate_site.py
lessons/index.html
assets
```

## Commit Message

```text
data: add validated L02 source-data JSON
```

## After Commit

Open a PR titled:

```text
data: add validated L02 source-data JSON
```

PR safety summary must say:

```text
- Adds only lesson-data/ca-life/u1-l2.json
- Does not commit raw Golden L02 HTML
- Does not modify public lesson HTML
- Does not modify homepage
- Validator passed
```
