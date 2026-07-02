# YSP Project Status

_Last checked: 2026-07-02_

## Current Project

YSP Learn & Shine is a GitHub Pages English-learning website.

```text
Repository: jobimtg/AT-vocab
Website: https://jobimtg.github.io/AT-vocab/
Brand: YSP Learn & Shine
Slogan: Learn with Purpose. Shine with Confidence.
Link-in-bio: https://beacons.ai/ysp_learn_and_shine
Instagram: https://www.instagram.com/ysp_learnandshine/
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
| Homepage | Done | Homepage now links to courses, free previews, Beacons link hub, Instagram, and trial lesson booking. |
| Lessons index | Done | Course sections and lesson cards exist. |
| Course folders | Done | `lessons/ca-life/`, `lessons/travel/`, and `lessons/business/` exist. |
| Global lesson navigation | Done | `js/ysp-global-nav.js` renders shared lesson nav, Back to Lessons, and Top button. |
| Site maintenance script | Done | `scripts/ysp_site_maintenance.py` exists and is called by the maintenance workflow. |
| Site validation script | Done | `scripts/ysp_validate_site.py` is connected to the maintenance workflow in report-only mode. |
| Progress dashboard | Done | Display-only dashboard shows current architecture and readiness. |
| Claude Code workflow | Paused | Not used because the project does not currently use Anthropic API credit. |
| ChatGPT + Local Codex workflow | Active | Primary workflow for future repo changes. |

## Existing Lesson Inventory

| Course | Page | Current Status | Phase 5 Note |
|---|---|---:|---|
| Canada Life & Career | `lessons/ca-life/u1-l1.html` | Active preview | Public preview exists; full JSON conversion pending. |
| Canada Life & Career | `lessons/ca-life/u1-l2.html` | Golden reference target | Full source-data JSON now exists at `lesson-data/ca-life/u1-l2.json`; raw Golden HTML is not committed. |
| Travel English | `lessons/travel/u1-l1.html` | Active preview | Existing content should be converted later. |
| Business English | `lessons/business/u1-l1.html` | Partial / needs refactor | Refactor after pipeline proof. |

## Phase 2 Status

```text
Phase 2 — Content production foundation: Complete
```

Phase 2 completed the planning and production foundation needed before mass lesson generation.

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

## Phase 4 Status

```text
Phase 4 — External Launch Setup: First IG soft campaign scheduled
```

Completed externally by user:

| Task | Status |
|---|---:|
| YSP Instagram profile created | Done |
| Beacons link-in-bio page created | Done |
| Beacons main buttons added | Done |
| Beacons button order checked | Done |
| Beacons link added to Instagram bio | Done |
| First 6 IG feed posts scheduled | Done |
| First campaign Stories scheduled | Done |

Manual external tasks still required later:

| Task | Status |
|---|---:|
| Payment / product platform setup | Pending |
| Practice Pack product upload | Pending |
| Add future product/payment links to homepage | Waiting for real URLs |

## Current Launch Flow

```text
Instagram
→ Beacons
→ YSP website / Free Preview Lessons / View Courses / Trial Lesson
```

## Current Campaign Flow

```text
Morning Stories
→ Evening Feed Posts
→ Link in bio
→ Beacons
→ Website / Free Preview / Trial Lesson
```

## Phase 5 Status

```text
Phase 5 — Lesson Factory: In progress
```

User-approved production direction:

```text
Future lessons should not be authored directly as HTML.
Use lesson-data JSON → fixed template → automatically generated HTML.
```

Phase 5 documents:

```text
docs/YSP_COURSE_ARCHITECTURE_REMAINING_WORK.md
docs/YSP_PHASE5_LESSON_FACTORY_GUIDE.md
```

Current Phase 5 work:

| Step | Task | Status |
|---:|---|---:|
| 5.1 | Full L02 source-data JSON | Done via PR #29 |
| 5.2 | Lesson data validator | Done via PR #30 |
| 5.3 | Fixed L02 template / renderer | Done via PR #31 |
| 5.4 | Lesson HTML builder | In PR |
| 5.5 | First generated proof lesson | Not started |
| 5.6 | Canada Life L03 source-data draft | Not started |

## Current Lesson Production Decision

Future lesson content should not be authored directly as HTML.

Current target architecture:

```text
lesson-data JSON / Markdown source
        ↓
validate_lesson_data.py
        ↓
fixed L02 renderer / template
        ↓
build_lesson_html.py
        ↓
generated lesson HTML
        ↓
GitHub Pages
```

HTML is the public output, not the main editing source.

## Current Phase 5 Data Status

```text
lesson-data/ca-life/u1-l2.json exists.
Raw Golden L02 HTML is not committed to the public repo.
The JSON file includes a validation block with passed counts.
templates/lesson-l02-template.html exists.
scripts/validate_lesson_data.py exists.
```

## Next Action

Recommended next step after Phase 5.4 merges:

```text
Phase 5.5 — Generate first safe proof lesson.
```
