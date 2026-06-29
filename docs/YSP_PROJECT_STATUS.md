# YSP Project Status

_Last checked: 2026-06-29_

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

## Current Architecture

| Area | Current Status | Notes |
|---|---:|---|
| GitHub Pages website | Done | Public site is live. |
| Homepage | Mostly done | Hero, course paths, featured preview lessons, About, CTA, footer, and Top button exist. |
| Lessons index | Mostly done | Course sections and auto-managed lesson cards exist. Some duplicate/placement cleanup may still be needed. |
| Course folders | Done | `lessons/ca-life/`, `lessons/travel/`, and `lessons/business/` exist. |
| Global lesson navigation | Mostly done | `js/ysp-global-nav.js` exists and renders shared lesson nav, Back to Lessons, and Top button. |
| Site maintenance script | Done | `scripts/ysp_site_maintenance.py` exists and is called by the maintenance workflow. |
| Site validation script | Done / needs workflow integration | `scripts/ysp_validate_site.py` exists, but should be connected to the workflow. |
| Progress dashboard | Exists / needs update | The workflow exists but still checks some older Step 1 items. |
| Claude Code workflow | Not done | Dedicated `.github/workflows/claude-code.yml` still needs to be added. |
| Issue template for AI tasks | Not done | Needed so future `@claude` tasks are structured and safe. |

## Completed

### Brand

| Item | Status |
|---|---:|
| Brand name: YSP Learn & Shine | Done |
| Slogan: Learn with Purpose. Shine with Confidence. | Done |
| Footer brand year: EST. 2026 | Done |
| Public positioning: Preview + Practice Pack + Trial Lesson | Done |

### Website Pages

| Page / Area | Status | Notes |
|---|---:|---|
| Homepage clean layout | Mostly done | Public layout is strong; auto-managed cards may need placement cleanup. |
| Homepage CTA structure | Done | Preview lesson and trial lesson CTAs exist. |
| Lessons page clean layout | Mostly done | Course sections exist; auto-managed lesson card section may need cleanup. |
| Course folders | Done | Canada Life, Travel, Business folders exist. |
| Canada Life L01 | Done / active | `lessons/ca-life/u1-l1.html` exists. |
| Travel L01 | Done / active | `lessons/travel/u1-l1.html` exists. |
| Business L01 | Partial | Page exists but uses an iframe/base64 structure and should later be refactored to the cleaner lesson template. |
| Lesson page global navigation | Mostly done | Shared JS loader exists on lesson pages. |
| Top button duplicate issue | Mostly done | Global nav JS removes legacy duplicates; needs validation after each workflow run. |
| Pronunciation image display | Partial | Some pages use direct image logic; automation and validation should be tightened. |

### Workflows

Current active custom workflows should remain:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

GitHub Pages deployment may also appear as the system deployment workflow.

| Item | Status | Notes |
|---|---:|---|
| Many patch workflows removed | Mostly done | Do not restore old patch workflows. |
| Maintenance workflow centralized | Done | Workflow now calls `scripts/ysp_site_maintenance.py`. |
| Progress dashboard display-only | Done / needs update | It displays status only but should be updated to current architecture. |
| Python moved out of maintenance YAML | Done | The maintenance YAML is short and calls the script. |
| Dedicated maintenance script | Done | `scripts/ysp_site_maintenance.py` exists. |
| Dedicated validation script | Done | `scripts/ysp_validate_site.py` exists. |
| Validation connected to workflow | Not done | Add workflow step later. |
| Dedicated Claude Code workflow | Not done | Add after docs are updated. |

## Not Completed Yet

### Engineering

| Item | Priority | Status |
|---|---:|---:|
| Update outdated project docs | High | In progress |
| Update `ysp-progress-dashboard.yml` for current architecture | High | Not done |
| Add validation step to maintenance workflow | High | Not done |
| Add dedicated Claude Code GitHub Action workflow | High | Not done |
| Add GitHub Issue template for YSP AI tasks | High | Not done |
| Add PR checklist for Claude/Codex changes | Medium | Not done |
| Prove maintenance idempotency by running it twice | High | Not done |
| Clean duplicate managed lesson-card placement on homepage / lessons page | High | Not done |
| Improve pronunciation / dynamic image gallery automation | Medium | Not done |

### Content Product

| Item | Priority | Status |
|---|---:|---:|
| First Free Preview Lesson model | High | Partial |
| First Full Practice Pack | High | Not done |
| Practice Pack PDF template | Medium | Not done |
| Test with existing students | Medium | Not done |
| Payment / purchase path | Low | Not done |

### Marketing / Conversion

| Item | Priority | Status |
|---|---:|---:|
| Beacons integration | Medium | Not done |
| Contact or waitlist form | Medium | Not done |
| SEO / Open Graph metadata | Medium | Not done |
| Payhip / Ko-fi / Gumroad decision | Low | Not done |

## Recommended Current Focus

Do not create more course pages yet.

Stabilize the AI + GitHub engineering system first:

```text
1. Update docs so Claude reads the correct project status.
2. Add Claude Code GitHub Action workflow.
3. Add GitHub Issue template for safe AI tasks.
4. Connect `scripts/ysp_validate_site.py` to the workflow.
5. Update the progress dashboard.
6. Clean duplicate managed lesson-card placement.
7. Run maintenance twice to confirm idempotency.
```

Then move to content production:

```text
L01 Free Preview Lesson
L01 Full Practice Pack
Student testing
Purchase or contact pathway
```
