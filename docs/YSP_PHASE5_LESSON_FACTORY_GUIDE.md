# YSP Phase 5 Lesson Factory Guide

_Last updated: 2026-07-02_

## User Decision Confirmed

The user approved this production direction:

```text
Future lessons should not be authored directly as HTML.
Use lesson-data JSON → fixed template → automatically generated HTML.
```

## What Phase 5 Is

Phase 5 builds the lesson-production factory.

It is not a public website feature for students. It is an internal production system that makes future lessons consistent, safer, and easier to maintain.

## Simple Model

| Role | Meaning |
|---|---|
| `lesson-data JSON` | Lesson content source: vocabulary, phrases, dialogues, speaking, culture, pronunciation |
| `fixed L02 template` | The Golden L02 layout and renderer that controls how every lesson looks |
| `builder script` | Tool that injects JSON data into the fixed template |
| `generated HTML` | Public lesson page served by GitHub Pages |
| `validator` | Quality-control tool that checks required counts and structure |

## Final Production Flow

```text
lesson-data JSON
        ↓
validate_lesson_data.py
        ↓
fixed L02 template / renderer
        ↓
build_lesson_html.py
        ↓
generated lesson HTML
        ↓
YSP Site Maintenance
        ↓
YSP Site Validator
        ↓
GitHub Pages
```

## What ChatGPT / Codex / GitHub Can Do Automatically

The user does not need to do these manually.

| Step | Auto Owner | Status |
|---:|---|---:|
| A1 | Create repo docs and tracking files | Done / ongoing |
| A2 | Create extraction scripts | Started |
| A3 | Create lesson-data validator | Next |
| A4 | Create fixed L02 template storage | Pending |
| A5 | Create HTML builder script | Pending |
| A6 | Run repo checks and compare changed files | Ongoing |
| A7 | Open and merge PRs when safe | Ongoing |
| A8 | Update project status files | Ongoing |
| A9 | Update lesson registry when lessons are added | Future |
| A10 | Generate future lesson HTML after source-data approval | Future |

## What The User Must Do Manually

Only these tasks require the user.

| Manual Step | What You Do | When |
|---:|---|---|
| U1 | Provide or confirm the Golden L02 HTML source file | Before full JSON extraction |
| U2 | Confirm that extracted L02 data looks correct enough to use as the standard | After JSON extraction report |
| U3 | Approve the fixed Golden L02 visual/template standard | Before generating new HTML |
| U4 | Approve first generated proof lesson before it replaces or publishes anything | After builder proof |
| U5 | Approve new lesson content topics before new source-data drafts | Before L03 / Travel L02 / Business refactor |
| U6 | Upload or provide lesson images when needed | Before image workflow / publication |
| U7 | Approve paid Practice Pack content before product upload | Before payment/product launch |

## What The User Should Not Need To Do

```text
Do not manually edit JSON.
Do not manually edit generated HTML.
Do not manually copy long data arrays.
Do not manually fix tab order.
Do not manually count Core / Extended / Dialogues / Speaking / Culture.
Do not manually update lessons/index.html.
Do not manually add duplicate navigation.
```

## Current Manual Step Needed

The current manual task is only:

```text
Confirm the correct Golden L02 source file is available for extraction.
```

Expected file name:

```text
L02_transportation_fixed_teacher_notes.html
```

After that, ChatGPT / Codex can handle the extraction and validation workflow.

## Current Auto Step In Progress

```text
Phase 5.1 — Full L02 Source-Data JSON
```

Target output:

```text
lesson-data/ca-life/u1-l2.json
```

Existing helper script:

```text
scripts/extract_l02_source_data.py
```

## Safe Execution Rule

Do not modify public lesson HTML until the source-data and validator pass.

This means:

```text
No public lesson HTML replacement yet.
No L03 HTML generation yet.
No Business L01 refactor yet.
No Practice Pack product link yet.
```

## Next Auto Steps

| Order | Step | Output |
|---:|---|---|
| 1 | Extract full L02 source-data JSON | `lesson-data/ca-life/u1-l2.json` |
| 2 | Create lesson-data validator | `scripts/validate_lesson_data.py` |
| 3 | Validate L02 JSON | validation report |
| 4 | Store fixed Golden L02 template | `templates/lesson-l02-template.html` |
| 5 | Create HTML builder | `scripts/build_lesson_html.py` |
| 6 | Generate proof HTML in safe draft path | draft output only |
| 7 | User reviews proof | manual approval |
| 8 | Start Canada Life L03 source-data draft | JSON first, not HTML first |

## User Checklist For Now

```text
[ ] Confirm the Golden L02 HTML file name is correct.
[ ] Confirm whether the Golden L02 source is allowed to be stored in the public repo.
[ ] Wait for extraction / validation result.
```

## Public Repo Warning

If the Golden L02 HTML file is committed into the GitHub repo, it may become publicly visible if the repo is public.

Safer options:

| Option | Use When |
|---|---|
| Keep source HTML local and run extraction locally | Best if the source should not be public |
| Commit source HTML into repo | Only if it is okay for the full source HTML to be public |
| Commit only extracted JSON | Good middle option if JSON is safe to be public |

## Recommended Choice

Recommended for this project:

```text
Do not publish the full raw L02 HTML source unless needed.
Use local extraction, then commit only validated lesson-data JSON.
```
