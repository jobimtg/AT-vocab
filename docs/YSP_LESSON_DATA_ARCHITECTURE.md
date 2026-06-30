# YSP Lesson Data Architecture

_Last updated: 2026-06-30_

## Purpose

This document locks the Phase 2 architecture decision:

```text
Do not use hand-written lesson HTML as the source of truth.
```

The public website may still display HTML because GitHub Pages serves HTML. However, the editable lesson source should be structured data.

## Core Architecture

Recommended production flow:

```text
lesson-data/*.json or lesson-data/*.md
        ↓
fixed L02 renderer / template
        ↓
generated lessons/.../u1-l2.html
        ↓
YSP Site Maintenance
        ↓
YSP Site Validator
        ↓
GitHub Pages
```

HTML is output, not the primary lesson-authoring format.

## Why Not Direct HTML?

Direct HTML generation caused repeated risks:

```text
layout drift
wrong tab order
wrong vocabulary-card classes
legacy .vocab-card output
wrong Core / Extended counts
missing SVGs
broken familiarity buttons
inconsistent image paths
duplicate navigation / Top buttons
hard-to-review lesson content changes
```

Phase 2 must prevent these issues by separating content from presentation.

## Source of Truth Layers

| Layer | Source | Purpose |
|---|---|---|
| Content source | `lesson-data/**/*.json` | Vocabulary, phrases, dialogues, speaking, culture, pronunciation |
| Template / renderer | future `templates/lesson-l02-template.html` | Fixed Golden L02 structure and rendering logic |
| Generated output | `lessons/{course}/uN-lN.html` | Public website HTML |
| Registry | `docs/YSP_LESSON_REGISTRY.md` | Tracks lesson status, path, CEFR, image prefix, source file |
| Validation | `scripts/ysp_validate_site.py` and future data validator | Ensures generated output is safe |

## Recommended Repository Structure

```text
lesson-data/
  ca-life/
    u1-l1.json
    u1-l2.json
  travel/
    u1-l1.json
    u1-l2.json
  business/
    u1-l1.json

templates/
  lesson-l02-template.html

scripts/
  build_lesson_html.py
  validate_lesson_data.py
  ysp_validate_site.py

docs/
  YSP_LESSON_REGISTRY.md
  YSP_GOLDEN_LESSON_TEMPLATE.md
  YSP_LESSON_DATA_ARCHITECTURE.md
```

## Lesson Data Format

The preferred source format is JSON.

Each lesson source file should contain:

```json
{
  "meta": {},
  "categories": [],
  "core": [],
  "extended": [],
  "phrases": [],
  "dialogues": [],
  "speaking": [],
  "culture": [],
  "pronunciation": {},
  "previously_learned": {}
}
```

## Mapping to v3.7 Renderer Variables

The builder should convert JSON into the v3.7 variables:

| JSON Field | Renderer Variable |
|---|---|
| `categories` | `CATS` |
| `core` | `V` |
| `extended` | `EXT` |
| `phrases` | `PHRASES` |
| `dialogues` | `DIALOGUES` |
| `speaking` | `SPEAKING` |
| `culture` | `CULTURE` |
| `pronunciation` | `PRON` |

## Metadata Schema

Recommended `meta` fields:

```json
{
  "course_id": "canada-en",
  "course_name": "Canada Life & Career English",
  "unit": 1,
  "lesson": 2,
  "lesson_code": "L02",
  "title_en": "Transportation in Canada",
  "title_zh": "加拿大交通",
  "cefr": "A2",
  "phase": "Phase 1",
  "html_path": "lessons/ca-life/u1-l2.html",
  "image_prefix": "l02",
  "status": "golden"
}
```

## Course Count Rules

The data validator must enforce:

| Course | CEFR | Core | Extended | Phrases | Dialogues | Speaking | Culture | Pronunciation |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Travel English | A1 | 15 | 30 | 5 | 5 | 5 | 2 | 1 |
| Canada Life & Career | A2 | 25 | 30 | 5 | 5 | 5 | 2 | 1 |
| Canada Life & Career | B1 | 30 | 30 | 5 | 5 | 5 | 2 | 1 |
| Business English | B2 | 40 | 30 | 5 | 5 | 5 | 2 | 1 |

## Build Rules

The builder must:

```text
read one lesson-data JSON file
validate required fields and counts
inject data into the fixed L02 renderer template
write one generated lesson HTML file
preserve YSP_GLOBAL_NAV_LOADER block
avoid manual nav / Top buttons
run site validator after generation
```

## What the Builder Must Not Do

The builder must not:

```text
rewrite unrelated lessons
modify homepage wording
modify lesson index manually
create duplicate nav
invent Previously Learned data
change lesson content outside the target lesson
write broken image paths
create per-lesson assets folders
```

## Image Workflow Relationship

Image workflow depends on this architecture.

Images should be managed by registry and prefix, not by memory.

Recommended future image workflow:

```text
image-inbox/
  ca-life-l02-pronunciation-1.png
  ca-life-l02-d01-model.png
  ca-life-l02-d01-practice.png

scripts/ysp_sort_images.py
  reads docs/YSP_LESSON_REGISTRY.md or lesson-data metadata
  moves files into course-level assets folders
  renames files to approved prefixes
```

Final image locations:

```text
lessons/ca-life/assets/pronunciation/l02-pronunciation-1.png
lessons/ca-life/assets/dialogues/l02-d01-model.png
lessons/ca-life/assets/dialogues/l02-d01-practice.png
```

## Phase 2 Implementation Order

Do not build everything at once.

Recommended order:

| Step | Output | Purpose |
|---:|---|---|
| 2.2A | `YSP_LESSON_DATA_ARCHITECTURE.md` | Lock source-data architecture |
| 2.2B | `YSP_LESSON_REGISTRY.md` | Track paths, status, prefixes |
| 2.2C | `lesson-data/README.md` | Define data folder use |
| 2.2D | one sample JSON from L02 | Prove data-source format |
| 2.2E | `templates/lesson-l02-template.html` | Store fixed renderer/template |
| 2.2F | `scripts/validate_lesson_data.py` | Validate JSON before build |
| 2.2G | `scripts/build_lesson_html.py` | Generate HTML output |
| 2.2H | image workflow plan/script | Auto-sort images safely |

## Current Decision

```text
Use JSON as the primary lesson source format.
Use HTML only as generated output.
Use L02 Golden Template as the fixed renderer target.
Do not hand-author future lessons directly in HTML.
```

## Next Step

Create:

```text
docs/YSP_LESSON_REGISTRY.md
```

Then convert L02 into a sample JSON source file for proof of concept.
