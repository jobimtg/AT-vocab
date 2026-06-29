# YSP Workflow Plan

_Last checked: 2026-06-29_

## Current Workflow Strategy

The project should keep a small workflow system. Do not restore the older patch-workflow setup.

Current custom workflows:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

GitHub Pages deployment may also appear as a system deployment workflow.

## Workflow 1 — YSP Site Maintenance

Path:

```text
.github/workflows/ysp-site-maintenance.yml
```

Purpose:

```text
Maintain lesson pages
Update lesson cards
Update homepage featured lessons
Attach global nav loader
Remove legacy generated blocks
Reduce duplicate nav / Top button problems
```

Current status:

```text
Done / active
```

The workflow now calls:

```text
python3 scripts/ysp_site_maintenance.py
```

This means the earlier refactor goal is complete. The maintenance YAML should remain short.

### Still Needed for Workflow 1

| Task | Priority | Status |
|---|---:|---:|
| Run `scripts/ysp_validate_site.py` after maintenance | High | Not done |
| Commit only safe generated changes | High | Mostly done |
| Confirm workflow is idempotent | High | Not done |
| Clean homepage / lessons card placement | High | Not done |
| Avoid changing lesson content | Critical | Ongoing rule |

## Workflow 2 — YSP Progress Dashboard

Path:

```text
.github/workflows/ysp-progress-dashboard.yml
```

Purpose:

```text
Display current progress in GitHub Actions Summary
Do not modify files
Do not commit
Do not create report folders
```

Current status:

```text
Exists / needs update
```

The dashboard should now check the current architecture, not older Step 1 workflow names.

### Dashboard Should Check

```text
index.html exists
lessons/index.html exists
js/ysp-global-nav.js exists
scripts/ysp_site_maintenance.py exists
scripts/ysp_validate_site.py exists
.github/workflows/ysp-site-maintenance.yml exists
.github/workflows/ysp-progress-dashboard.yml exists
old patch workflows are removed
no report folder exists
at least one lesson exists
at least one lesson has global nav loader
```

### Dashboard Should Stop Treating These as Required

```text
step1-revenue-positioning.yml
auto-update-lessons-clean-header.yml
update-ysp-progress-tracker.yml
.github/workflow-reports/
```

## Workflow 3 — Claude Code GitHub Action

Path to add later:

```text
.github/workflows/claude-code.yml
```

Purpose:

```text
Allow GitHub Issues / PRs to trigger Claude Code with @claude.
Claude should read CLAUDE.md and docs/YSP_*.md first.
Claude should create PRs, not push directly to main.
```

Current status:

```text
Not done
```

Before adding this workflow, confirm the repo has the required Anthropic secret in GitHub Actions secrets:

```text
ANTHROPIC_API_KEY
```

Do not put the API key in the repo.

## Recommended AI Development Flow

```text
GitHub Issue → @claude → Claude creates branch/PR → Actions validate → user reviews → merge
```

Use ChatGPT / Codex for review and planning. Use Claude Code GitHub Action for repo-editing tasks once configured.

## Old Workflows Not To Restore

Do not restore:

```text
auto-update-lessons-after-upload.yml
refresh-lesson-navigation.yml
check-course-links-v3-report-only.yml
check-course-links-v2.yml
check-site-links.yml
add-lesson-navigation.yml
add-lesson-navigation-v2.yml
auto-update-lessons-clean-header.yml
clean-homepage-layout.yml
clean-lessons-layout.yml
fix-top-button-overlap.yml
fix-practice-pack-placement.yml
fix-revenue-sections-placement.yml
fix-step1-sections-placement-combined.yml
step1-revenue-positioning.yml
update-ysp-progress-tracker.yml
```

## Next Workflow Tasks

| Order | Task | Files | Status |
|---:|---|---|---:|
| 1 | Update project tracking docs | `docs/*.md`, `README_CLAUDE_CODE_HANDOFF.md` | In progress |
| 2 | Add Claude Code workflow | `.github/workflows/claude-code.yml` | Not done |
| 3 | Add YSP task issue template | `.github/ISSUE_TEMPLATE/ysp-ai-task.yml` | Not done |
| 4 | Add validation to maintenance workflow | `.github/workflows/ysp-site-maintenance.yml` | Not done |
| 5 | Update progress dashboard checks | `.github/workflows/ysp-progress-dashboard.yml` | Not done |
| 6 | Clean duplicate managed card placement | `scripts/ysp_site_maintenance.py`, `index.html`, `lessons/index.html` | Not done |
| 7 | Run idempotency test | Workflow + local script behavior | Not done |

## Do Not Do Yet

Do not start these until workflow safety is stable:

```text
Add many new lessons
Refactor every lesson page
Build payment pages
Add Beacons integration
Add AdSense
Add large marketing sections
```
