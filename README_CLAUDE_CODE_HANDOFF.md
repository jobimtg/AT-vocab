# Claude Code Handoff — How to Use This Package

_Last checked: 2026-06-29_

## Files in this package

```text
CLAUDE.md
README_CLAUDE_CODE_HANDOFF.md
docs/YSP_PROJECT_STATUS.md
docs/YSP_SITE_RULES.md
docs/YSP_WORKFLOW_PLAN.md
docs/YSP_CLAUDE_CODE_TASKS.md
```

## Where they live

These files should stay in the root of the `AT-vocab` repository.

Final structure:

```text
AT-vocab/
  CLAUDE.md
  README_CLAUDE_CODE_HANDOFF.md
  docs/
    YSP_PROJECT_STATUS.md
    YSP_SITE_RULES.md
    YSP_WORKFLOW_PLAN.md
    YSP_CLAUDE_CODE_TASKS.md
```

## Current Repo Status

Important update:

```text
The old first engineering task is already mostly complete.
```

Do not ask Claude Code to redo the old Task 1 unless the workflow is broken again.

Current confirmed files:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
scripts/ysp_site_maintenance.py
scripts/ysp_validate_site.py
js/ysp-global-nav.js
```

Current next focus:

```text
1. Add Claude Code GitHub Action workflow.
2. Add YSP AI task issue template.
3. Connect validation script to maintenance workflow.
4. Update progress dashboard checks.
5. Clean duplicate managed lesson-card placement.
6. Run idempotency test.
```

## Open Claude Code Locally

In PowerShell:

```powershell
cd $HOME\Documents\GitHub\AT-vocab
claude
```

## First Prompt to Claude Code

Use this first:

```text
Read CLAUDE.md and all docs/YSP_*.md files first. Do not edit anything yet. Summarize the current project state, current risks, and the first safe task based on the latest docs.
```

## Safe Working Rule

Do not ask Claude Code to fix everything at once.

Use this pattern:

```text
Read first.
Summarize first.
Plan first.
Edit one task.
Validate.
Commit or open PR.
Move to next task.
```

## Do Not Let Claude Code Do This

```text
Rewrite all lesson content
Restore old workflows
Create report folders
Add many new workflows
Redesign the whole website
Delete lesson sections
Change teaching materials without permission
Push directly to main without review
```

## Recommended GitHub Issue Prompt After Claude Code Action Is Installed

Use this format inside a GitHub Issue:

```text
@claude

Read CLAUDE.md and all docs/YSP_*.md files first.

Task: <one clear task only>

Allowed files to modify:
- <file 1>
- <file 2>

Do not modify:
- lesson content
- public lesson text
- vocabulary/dialogue/speaking/culture content
- unrelated workflows

Before editing, summarize:
1. Files you will modify
2. Why those files need modification
3. What will not be changed
4. How you will verify the result

After editing, open a PR with:
- Summary
- Files changed
- Validation result
- Remaining risks
```

## Recommended Next Engineering Milestone

Complete these tasks in order:

```text
1. Add `.github/workflows/claude-code.yml`.
2. Add `.github/ISSUE_TEMPLATE/ysp-ai-task.yml`.
3. Update `.github/workflows/ysp-site-maintenance.yml` to run `scripts/ysp_validate_site.py`.
4. Update `.github/workflows/ysp-progress-dashboard.yml` for current checks.
5. Clean duplicate managed card placement in `index.html` and `lessons/index.html`.
6. Run maintenance twice and confirm the second run creates no changes.
```

Then proceed to content production:

```text
L01 Free Preview Lesson
L01 Full Practice Pack
Student testing
Purchase or contact pathway
```
