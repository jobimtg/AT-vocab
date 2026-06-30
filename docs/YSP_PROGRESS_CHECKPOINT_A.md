# YSP Progress Checkpoint A

_Last updated: 2026-06-30_

## Purpose

This checkpoint reconciles the older AT website architecture task list with the current repository state.

It confirms which engineering tasks are complete, which tasks have moved into Phase 2, and which tasks should not be mixed with the current checkpoint.

## Current Decision

```text
Phase 1 Website Automation Foundation: Complete
Checkpoint A: Complete
```

The site engineering foundation is stable enough to move into Phase 2 content architecture and product planning.

## Old Task List Reconciliation

| Order | Task | Old Status | Current Status | Current Notes |
|---:|---|---:|---:|---|
| Step 1 | Branch / Workflow Check | ✅ Complete | ✅ Complete | `main` is active and GitHub workflow foundation has been verified. |
| Task 1 | Extract maintenance script | ✅ Complete | ✅ Complete | `scripts/ysp_site_maintenance.py` exists and is called by `ysp-site-maintenance.yml`. |
| Task 1-B | GitHub Actions check | ✅ Complete | ✅ Complete | `YSP Site Maintenance` runs successfully and is idempotent. |
| Task 2 | Global Nav audit | ✅ Complete | ✅ Complete | Lesson pages use the global nav loader. |
| Task 2-B | Sticky global nav | ✅ Complete | ✅ Complete | `js/ysp-global-nav.js` creates one sticky website nav, one Back to Lessons link, and one Top button. |
| Task 2-C | Live sticky nav check | ✅ Complete | ✅ Complete | Confirmed by user screenshot during Phase 1. |
| Task 3 | Pronunciation image audit | ✅ Complete | ✅ Complete | L01 image references were found and validated by the site validator. |
| Task 3-B | Add L01 pronunciation image | ✅ Complete | ✅ Complete | `lessons/ca-life/u1-l1.html` references `assets/pronunciation/l01-pronunciation-1.png`. |
| Checkpoint A | Tasks 1–3 final audit | ⏳ Next | ✅ Complete | Replaced by Phase 1 final validation: dashboard 100%, validator 0 errors / 0 warnings. |
| Task 4 | Progress Dashboard cleanup | ⏸ Not started | ✅ Complete | `ysp-progress-dashboard.yml` now reflects the current architecture and shows 100% readiness. |
| Task 5 | Validator strengthening | ⏸ Not started | ✅ Complete baseline | `scripts/ysp_validate_site.py` is connected to maintenance workflow in report-only mode. Future upgrade to blocking validation is optional. |
| Image Workflow | `image-inbox` + registry + auto-sort | ⏸ Not started | ⏳ Phase 2 planning | Do not implement auto-sort until lesson data architecture and registry are locked. |
| Task 8 | L01 Preview / Practice Pack | ⏸ Later | ⏳ Product phase | Should happen after data architecture, registry, and course production rules are finished. |

## Evidence Summary

Confirmed current repo state:

```text
.github/workflows/ysp-site-maintenance.yml exists
scripts/ysp_site_maintenance.py exists
scripts/ysp_validate_site.py exists
js/ysp-global-nav.js exists
YSP Progress Dashboard reached 100%
YSP Site Validator reached 0 errors / 0 warnings
Lesson pages with global loader reached 3/3
```

## Checkpoint A Result

```text
Checkpoint A is complete.
```

The original Checkpoint A goal was to confirm that Tasks 1–3 were clean before progressing to dashboard cleanup and validator strengthening.

That has now been surpassed:

```text
Dashboard cleanup: complete
Validator connection: complete
Maintenance idempotency: verified
```

## Remaining Items That Should Not Be Treated as Phase 1 Blockers

### Image Workflow

The image workflow is still important, but it belongs to Phase 2 because it depends on the lesson registry and lesson data architecture.

Recommended Phase 2 image workflow:

```text
image-inbox/
lesson registry
image naming convention
auto-sort script
course-level assets folders
validation of rendered image paths
```

### L01 Preview / Practice Pack

The L01 Preview / Practice Pack is a product task, not a website-foundation task.

It should start after:

```text
1. Lesson Data Architecture
2. Lesson Registry
3. Course Production Rules
4. Golden L02 renderer / template path
```

## Next Engineering Step

Create the lesson source architecture:

```text
docs/YSP_LESSON_DATA_ARCHITECTURE.md
```

The key decision:

```text
Lesson content source should not be hand-edited HTML.
HTML should be generated output.
```
