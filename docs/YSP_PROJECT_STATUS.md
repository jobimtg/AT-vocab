# YSP Project Status

_Last checked: 2026-06-30_

## Current Project

YSP Learn & Shine is a GitHub Pages English-learning website.

```text
Repository: jobimtg/AT-vocab
Website: https://jobimtg.github.io/AT-vocab/
Brand: YSP Learn & Shine
Slogan: Learn with Purpose. Shine with Confidence.
```

## Current Direction

This site should stay low-maintenance and stable. It is not meant to become a full free course database.

The current public website positioning is:

```text
Free Preview Lessons
Full Practice Packs
Guided Trial Lessons
```

## Phase 1 Status

```text
Phase 1 — Website automation foundation: Complete
```

Confirmed Phase 1 completion:

| Area | Status |
|---|---:|
| Website automation architecture | Done |
| Progress dashboard | Done |
| YSP Site Maintenance workflow | Done |
| YSP Site Validator | Done |
| Validation connected to maintenance workflow | Done |
| Global lesson loader | Done |
| Duplicate footer managed sections | Fixed |
| Managed stylesheet cleanup | Fixed |
| Maintenance idempotency | Verified |
| Claude GitHub Action | Paused by project decision |
| ChatGPT + Local Codex workflow | Active workflow |
| YSP AI task issue template | Done |

Final Phase 1 verification:

```text
Current Website / Automation Architecture: 100%
Next Engineering Readiness: 100%
Lesson Pages With Global Loader: 3/3
YSP Site Validator: 0 errors, 0 warnings
YSP Site Maintenance: no repeated changes
```

## Current Active Workflows

Only these custom workflows should remain active:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

GitHub Pages deployment may also appear as the system deployment workflow.

## Current Architecture

| Area | Current Status | Notes |
|---|---:|---|
| GitHub Pages website | Done | Public site is live. |
| Homepage | Done | Homepage now has a clearer product path for courses, free previews, practice packs, and trial lessons. |
| Lessons index | Done | Course sections and lesson cards exist. |
| Course folders | Done | `lessons/ca-life/`, `lessons/travel/`, and `lessons/business/` exist. |
| Global lesson navigation | Done | `js/ysp-global-nav.js` renders shared lesson nav, Back to Lessons, and Top button. |
| Site maintenance script | Done | `scripts/ysp_site_maintenance.py` exists and is called by the maintenance workflow. |
| Site validation script | Done | `scripts/ysp_validate_site.py` is connected to the maintenance workflow in report-only mode. |
| Progress dashboard | Done | Display-only dashboard shows current architecture and readiness. |
| Claude Code workflow | Paused | Not used because the project does not currently use Anthropic API credit. |
| ChatGPT + Local Codex workflow | Active | Primary workflow for future repo changes. |

## Existing Lesson Inventory

| Course | Page | Current Status | Phase 2 Note |
|---|---|---:|---|
| Canada Life & Career | `lessons/ca-life/u1-l1.html` | Active preview | Registered as `active-preview`; not final Golden source. |
| Canada Life & Career | `lessons/ca-life/u1-l2.html` | Golden reference target | Uploaded L02 is Golden source; schema-proof manifest exists. |
| Travel English | `lessons/travel/u1-l1.html` | Active preview | Registered as `active-preview`; older structure should not drive future lessons. |
| Business English | `lessons/business/u1-l1.html` | Partial / needs refactor | Refactor plan complete; implementation later. |

## Phase 2 Status

```text
Phase 2 — Content production foundation: Complete
```

Phase 2 completed the planning and production foundation needed before mass lesson generation.

Primary Phase 2 documents:

```text
docs/YSP_PHASE2_CONTENT_PLAN.md
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

## Phase 2 Completion Table

| Step | Task | Status |
|---:|---|---:|
| 2.1 | Golden Lesson Template Audit | Complete baseline |
| 2.2A | Lesson Data Architecture | Complete |
| 2.2B | Lesson Registry | Complete baseline |
| 2.2C | L02 Source-Data Proof | Complete schema proof |
| 2.3 | Course Production Rules | Complete |
| 2.4 | Business L01 Refactor Plan | Complete |
| 2.5 | First New Lesson Draft Plan | Complete |
| 2.6 | Image Gallery / Asset Checklist | Complete |
| 2.7 | Practice Pack Template | Complete |
| Homepage | Homepage Revision Plan | Complete |

## Current Lesson Production Decision

Future lesson content should not be authored directly as HTML.

Current target architecture:

```text
lesson-data JSON / Markdown source
        ↓
fixed L02 renderer / template
        ↓
generated lesson HTML
        ↓
GitHub Pages
```

HTML is the public output, not the main editing source.

## Important Limitation

The full L02 data extraction into `lesson-data/ca-life/u1-l2.json` should be done by local Codex or a repo extraction script from the uploaded Golden L02 file.

The current repo contains a schema-proof manifest:

```text
lesson-data/ca-life/u1-l2.schema-proof.json
```

This avoids manually retyping large L02 arrays and SVG strings through the GitHub connector.

## Phase 3 Status

```text
Phase 3 — Product + Marketing website implementation: Complete in repo
```

Completed in repo:

| Task | Status |
|---|---:|
| Homepage monetization update | Done |
| Hero CTA update | Done |
| Courses / Free Preview / Trial Lesson path | Done |
| Free Preview / Practice Pack / Guided Trial Lesson explanation | Done |
| Phase 3 completion report | Done |

External manual tasks still required:

```text
YSP social profile setup
Link-in-bio setup
Payment / product platform setup
Practice Pack product upload
```

## Next Phase

Recommended next phase:

```text
Phase 4 — External Launch Setup
```

First Phase 4 candidates:

```text
1. Create YSP social profile manually.
2. Create link-in-bio page manually.
3. Choose payment / product platform.
4. Add real external links to homepage after they exist.
5. Use local Codex to extract full L02 JSON source.
```
