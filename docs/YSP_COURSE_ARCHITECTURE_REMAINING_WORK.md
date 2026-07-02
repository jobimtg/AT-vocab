# YSP Course Architecture Remaining Work

_Last updated: 2026-07-02_

## Purpose

This document returns the project focus from marketing launch back to website and lesson architecture.

The website foundation and launch path are stable. The remaining work is the actual course-production pipeline.

## Completed Website / Launch Foundation

| Area | Status |
|---|---:|
| GitHub Pages website | Complete |
| Homepage product path | Complete |
| Lessons index | Complete |
| Course folders | Complete |
| Global lesson navigation | Complete |
| Site maintenance workflow | Complete |
| Site validator baseline | Complete |
| Progress dashboard | Complete |
| Beacons link connected | Complete |
| Instagram link connected | Complete |
| First IG soft campaign scheduled | Complete |

## Remaining Course Architecture Work

| Priority | Workstream | Status | Why It Matters |
|---:|---|---:|---|
| 1 | Full L02 source-data JSON | Started | Converts Golden L02 from HTML-only into reusable lesson data. |
| 2 | Store fixed L02 renderer / template | Not started | Needed so future lessons use the same structure instead of AI-generated layout drift. |
| 3 | Lesson data validator | Not started | Checks required counts, fields, CEFR rules, and missing sections before HTML generation. |
| 4 | Lesson HTML builder | Not started | Generates public HTML from JSON + fixed template. |
| 5 | First generated lesson proof | Not started | Proves JSON → template → generated HTML works safely. |
| 6 | Canada Life L03 source-data draft | Not started | First new source-data lesson after L02 pipeline proof. |
| 7 | Business L01 clean refactor | Not started | Existing Business L01 uses iframe/base64 and should not remain the production pattern. |
| 8 | Image workflow auto-sort | Not started | Needs registry + source data to avoid image path drift. |
| 9 | Practice Pack source template | Not started | Needed before paid product upload. |
| 10 | Payment/product link integration | Waiting | Should only happen after real Practice Pack product exists. |

## Current Lesson Source Status

| Lesson | HTML Status | Source Data Status | Notes |
|---|---:|---:|---|
| Canada Life L01 | Active preview | Missing full JSON | Public preview exists, but not source-data converted. |
| Canada Life L02 | Golden reference | Schema proof exists; full extraction started | Golden L02 is the first source-data proof target. |
| Travel L01 | Active preview | Missing full JSON | Existing content should be converted later. |
| Business L01 | Needs refactor | Missing full JSON | Refactor after pipeline proof. |

## Next Step Started

```text
Phase 5.1 — Full L02 Source-Data JSON
```

Target file:

```text
lesson-data/ca-life/u1-l2.json
```

The source is the uploaded Golden L02 file:

```text
L02_transportation_fixed_teacher_notes.html
```

## Current Blocking Detail

The GitHub connector can safely update text files, but large extracted JSON arrays from the uploaded HTML should be handled carefully.

Recommended safe path:

```text
1. Extract L02 arrays locally with Codex or script.
2. Commit full lesson-data/ca-life/u1-l2.json.
3. Add scripts/validate_lesson_data.py.
4. Validate source-data counts before any HTML generation.
```

## Safety Rule

Do not generate or modify public lesson HTML until the source-data JSON and validator are stable.

## Next Step After Phase 5.1

```text
Phase 5.2 — Lesson Data Validator
```

Target file:

```text
scripts/validate_lesson_data.py
```
