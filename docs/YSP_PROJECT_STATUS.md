# YSP Project Status

_Last checked: 2026-07-01_

## Current Project

YSP Learn & Shine is a GitHub Pages English-learning website.

```text
Repository: jobimtg/AT-vocab
Website: https://jobimtg.github.io/AT-vocab/
Brand: YSP Learn & Shine
Slogan: Learn with Purpose. Shine with Confidence.
Link-in-bio: https://beacons.ai/ysp_learn_and_shine
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
| Homepage | Done | Homepage now links to courses, free previews, Beacons link hub, and trial lesson booking. |
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
Phase 4 — External Launch Setup: In progress
```

Completed in repo:

| Task | Status |
|---|---:|
| External launch checklist | Done |
| Homepage link rule documented | Done |
| No placeholder external links rule | Done |
| Confirmed Beacons link documented | Done |
| Beacons link added to homepage | Done |

Manual external tasks still required:

| Task | Status |
|---|---:|
| YSP social profile setup | Pending |
| Link-in-bio page setup | Done / user confirmation needed for button contents |
| Payment / product platform setup | Pending |
| Practice Pack product upload | Pending |
| Add future social/profile/product links to homepage | Waiting for real URLs |

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

## Next Action

Manual external setup:

```text
1. Confirm Beacons button contents and links.
2. Set up the YSP social profile.
3. Add the Beacons link to the YSP social profile bio.
4. Choose the product/payment platform.
5. Return with the real social/profile/product URLs so the homepage can be updated safely.
```
