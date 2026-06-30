# YSP Phase 2 Content Plan

_Last updated: 2026-06-30_

## Phase 2 Result

```text
Phase 2 Foundation: Complete
```

Phase 2 moved the project from website automation foundation into controlled lesson-production planning.

The goal was not to publish many new lessons quickly. The goal was to create a repeatable, safe lesson-production system that keeps every lesson visually consistent, technically valid, pedagogically useful, and aligned with YSP Learn & Shine.

## Phase 1 Completion Gate

Phase 1 is complete.

Confirmed foundation:

```text
Website automation architecture: 100%
Next engineering readiness: 100%
Lesson pages with global loader: 3/3
YSP Site Validator: 0 errors, 0 warnings
YSP Site Maintenance: idempotent, no repeated changes
```

## Current Source of Truth

The current technical and production source of truth is:

```text
CLAUDE.md
docs/YSP_SITE_RULES.md
docs/YSP_PROJECT_STATUS.md
docs/YSP_WORKFLOW_PLAN.md
docs/YSP_CLAUDE_CODE_TASKS.md
README_CLAUDE_CODE_HANDOFF.md
docs/YSP_GOLDEN_LESSON_TEMPLATE.md
docs/YSP_ESL_SKILL_SOURCE_MAP.md
docs/YSP_LESSON_DATA_ARCHITECTURE.md
docs/YSP_LESSON_REGISTRY.md
docs/YSP_COURSE_PRODUCTION_RULES.md
docs/YSP_BUSINESS_L01_REFACTOR_PLAN.md
docs/YSP_FIRST_NEW_LESSON_DRAFT.md
docs/YSP_IMAGE_WORKFLOW_AND_ASSET_CHECKLIST.md
docs/YSP_PRACTICE_PACK_TEMPLATE.md
docs/YSP_HOMEPAGE_REVISION_PLAN.md
docs/YSP_PHASE2_COMPLETION_REPORT.md
```

For Phase 2 lesson production, the most important rules are:

```text
Do not rewrite lesson content unless explicitly requested.
Do not remove vocabulary, dialogues, speaking questions, culture notes, or JavaScript lesson data.
Do not replace original text content with image galleries.
Do not create duplicate navigation, Back to Lessons, or Top buttons.
Use course-level assets folders only.
Use relative paths only.
Keep YSP Site Maintenance idempotent.
Run validation after technical changes.
Use lesson-data source files as the long-term source of truth.
Treat generated HTML as public website output, not the primary authoring source.
```

## Existing Lesson Inventory

| Course | File | Current Status | Phase 2 Action |
|---|---|---:|---|
| Canada Life & Career | `lessons/ca-life/u1-l1.html` | Active preview lesson | Keep as public preview; do not use as final Golden source without audit |
| Canada Life & Career | `lessons/ca-life/u1-l2.html` | Golden reference target | Uploaded L02 is Golden source; schema-proof manifest exists |
| Travel English | `lessons/travel/u1-l1.html` | Active preview lesson | Compare against future Travel template standard |
| Business English | `lessons/business/u1-l1.html` | Partial / iframe-base64 structure | Refactor plan complete; implementation later |

## Important Phase 2 Decision

Do not start by generating many new lessons.

Use this future production flow:

```text
lesson-data JSON / Markdown source
        ↓
fixed L02 renderer / template
        ↓
generated lesson HTML
        ↓
YSP Site Maintenance
        ↓
YSP Site Validator
        ↓
GitHub Pages
```

HTML is public output, not the primary authoring source.

## Phase 2 Completed Outputs

| Step | Task | Output | Status |
|---:|---|---|---:|
| 2.1 | Golden Lesson Template Audit | `docs/YSP_GOLDEN_LESSON_TEMPLATE.md` | Complete baseline |
| 2.2A | Lesson Data Architecture | `docs/YSP_LESSON_DATA_ARCHITECTURE.md` | Complete |
| 2.2B | Lesson Registry | `docs/YSP_LESSON_REGISTRY.md` | Complete baseline |
| 2.2C | L02 Source-Data Proof | `lesson-data/ca-life/u1-l2.schema-proof.json` | Complete schema proof |
| 2.3 | Course Production Rules | `docs/YSP_COURSE_PRODUCTION_RULES.md` | Complete |
| 2.4 | Business L01 Refactor Plan | `docs/YSP_BUSINESS_L01_REFACTOR_PLAN.md` | Complete |
| 2.5 | First New Lesson Draft Plan | `docs/YSP_FIRST_NEW_LESSON_DRAFT.md` | Complete |
| 2.6 | Image Gallery / Asset Checklist | `docs/YSP_IMAGE_WORKFLOW_AND_ASSET_CHECKLIST.md` | Complete |
| 2.7 | Practice Pack Template | `docs/YSP_PRACTICE_PACK_TEMPLATE.md` | Complete |
| Homepage | Homepage Revision Plan | `docs/YSP_HOMEPAGE_REVISION_PLAN.md` | Complete |
| Report | Phase 2 Completion Report | `docs/YSP_PHASE2_COMPLETION_REPORT.md` | Complete |

## Important Limitation

The uploaded L02 file was verified as the Golden Template source. A schema-proof manifest exists in the repo.

The full L02 data extraction into `lesson-data/ca-life/u1-l2.json` should be done with local Codex or a repo extraction script because the full source contains large JavaScript arrays and SVG strings.

Do not manually retype the full L02 arrays in chat.

## Phase 3 Recommended Start

Recommended next phase:

```text
Phase 3 — Product + Marketing Implementation
```

First candidates:

```text
1. Homepage monetization update
2. New YSP English IG + Beacons setup
3. Full L02 JSON extraction with local Codex
4. Build script / renderer proof of concept
5. First source-data generated lesson
```
