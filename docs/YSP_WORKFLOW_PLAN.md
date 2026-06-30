# YSP Workflow Plan

_Last checked: 2026-06-30_

## Current Workflow Strategy

The project should keep a small, low-cost workflow system. Do not restore the older patch-workflow setup.

Current active custom workflows:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

GitHub Pages deployment may also appear as the system deployment workflow.

## Current AI Development Strategy

Anthropic Claude GitHub Action was tested successfully at the GitHub setup level, but the run failed because the Anthropic API account had insufficient API credit.

The project is not using Anthropic API credit now.

Current AI workflow:

```text
Primary: ChatGPT GitHub connector for repo inspection, branches, PRs, and safe edits
Secondary: Local Codex on the user's computer for larger repo edits and local validation
Paused: Claude GitHub Action / @claude issue automation
```

Local Codex repo path:

```text
C:\Users\rose_\Desktop\Claude Skills\GitHub\AT-vocab
```

Do not use `@claude` Issue automation unless Anthropic API billing is intentionally re-enabled later.

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

Path:

```text
.github/workflows/claude-code.yml
```

Current status:

```text
Paused / not recommended for current project budget
```

Reason:

```text
GitHub App installation worked.
ANTHROPIC_API_KEY was detected.
OIDC permission was fixed.
But Claude Code returned: Credit balance is too low.
The user does not want to add Anthropic API credit.
```

Decision:

```text
Do not continue relying on Claude GitHub Action.
Use ChatGPT GitHub connector and local Codex instead.
```

Note:

```text
The workflow file may still exist in the repository, but @claude issue automation should not be used unless API billing is re-enabled later.
```

## Recommended ChatGPT + Local Codex Flow

### ChatGPT GitHub Flow

Use this when the user wants a safe remote PR:

```text
User gives task in ChatGPT
ChatGPT inspects repo
ChatGPT creates branch
ChatGPT edits limited files
ChatGPT opens PR
User reviews
User or ChatGPT merges
```

Best for:

```text
Docs updates
Small workflow fixes
Small HTML/script changes
Repo review
PR planning
```

### Local Codex Flow

Use this when the user wants to work from their computer:

```powershell
cd "C:\Users\rose_\Desktop\Claude Skills\GitHub\AT-vocab"
git pull origin main
git checkout -b codex/<task-name>
codex
```

Codex should always read first:

```text
CLAUDE.md
docs/YSP_PROJECT_STATUS.md
docs/YSP_WORKFLOW_PLAN.md
docs/YSP_CLAUDE_CODE_TASKS.md
docs/YSP_SITE_RULES.md
README_CLAUDE_CODE_HANDOFF.md
```

Codex must not change:

```text
lesson content
vocabulary text
dialogue text
speaking questions
culture text
brand wording unless requested
unrelated workflows
```

After Codex edits locally:

```powershell
git status
git diff
python scripts/ysp_validate_site.py
git add <changed-files>
git commit -m "<clear message>"
git push -u origin codex/<task-name>
```

Then open a PR on GitHub.

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
fix-revenue-sections-placement-combined.yml
step1-revenue-positioning.yml
update-ysp-progress-tracker.yml
```

## Next Workflow Tasks

| Order | Task | Files | Preferred tool | Status |
|---:|---|---|---|---:|
| 1 | Update project tracking docs | `docs/*.md`, `README_CLAUDE_CODE_HANDOFF.md` | ChatGPT | Done |
| 2 | Pause Claude GitHub Action usage | GitHub Actions settings / `.github/workflows/claude-code.yml` | GitHub UI or Codex | In progress |
| 3 | Add YSP task issue template for ChatGPT/Codex tasks | `.github/ISSUE_TEMPLATE/ysp-ai-task.yml` | ChatGPT | Not done |
| 4 | Add validation to maintenance workflow | `.github/workflows/ysp-site-maintenance.yml` | ChatGPT / Codex | Not done |
| 5 | Update progress dashboard checks | `.github/workflows/ysp-progress-dashboard.yml` | ChatGPT / Codex | Not done |
| 6 | Clean duplicate managed card placement | `scripts/ysp_site_maintenance.py`, `index.html`, `lessons/index.html` | Codex local preferred | Not done |
| 7 | Run idempotency test | Workflow + local script behavior | Codex local preferred | Not done |

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
