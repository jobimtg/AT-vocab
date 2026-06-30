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
| Homepage | Done | Hero, course paths, featured preview lessons, About, CTA, footer, and Top button exist. |
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
| Canada Life & Career | `lessons/ca-life/u1-l1.html` | Active | Current reference candidate after audit. |
| Travel English | `lessons/travel/u1-l1.html` | Active | Compare with future Travel template standard. |
| Business English | `lessons/business/u1-l1.html` | Partial | Uses iframe/base64 structure and should be refactored later. |

## Phase 2 Status

```text
Phase 2 — Content production and lesson expansion: Started
```

Phase 2 should not begin with mass lesson generation.

First, lock the reusable lesson standard and content-production rules.

Primary Phase 2 planning document:

```text
docs/YSP_PHASE2_CONTENT_PLAN.md
```

## Phase 2 Recommended Order

| Step | Task | Status |
|---:|---|---:|
| 2.1 | Golden Lesson Template Audit | In progress |
| 2.2 | Lesson Registry | Not started |
| 2.3 | Course Production Rules | Not started |
| 2.4 | Business L01 Refactor Plan | Not started |
| 2.5 | First New Lesson Draft | Not started |
| 2.6 | Image Gallery / Asset Checklist | Not started |
| 2.7 | Practice Pack Template | Not started |

## Phase 2 Safety Rule

Do not rewrite lesson content unless the user explicitly approves a content update task.

Do not modify:

```text
vocabulary text
dialogue text
speaking questions
culture text
lesson JavaScript data
student-facing lesson content
```

unless the task explicitly allows content editing.

## Next Action

Create the Golden Lesson Template audit document:

```text
docs/YSP_GOLDEN_LESSON_TEMPLATE.md
```

This document should define the exact reusable lesson structure before new lessons are created.
