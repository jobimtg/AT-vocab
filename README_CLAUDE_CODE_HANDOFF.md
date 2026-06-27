# Claude Code Handoff — How to Use This Package

## Files in this package

```text
CLAUDE.md
docs/YSP_PROJECT_STATUS.md
docs/YSP_SITE_RULES.md
docs/YSP_WORKFLOW_PLAN.md
docs/YSP_CLAUDE_CODE_TASKS.md
README_CLAUDE_CODE_HANDOFF.md
```

## Where to place them

Place them in the root of the `AT-vocab` repository.

Final structure:

```text
AT-vocab/
  CLAUDE.md
  docs/
    YSP_PROJECT_STATUS.md
    YSP_SITE_RULES.md
    YSP_WORKFLOW_PLAN.md
    YSP_CLAUDE_CODE_TASKS.md
```

## Open Claude Code

In PowerShell:

```powershell
cd $HOME\Documents\GitHub\AT-vocab
claude
```

## First prompt to Claude Code

Use this first:

```text
Read CLAUDE.md and all docs/YSP_*.md files first. Do not edit anything yet. Summarize the project state, current risks, and the first safe task.
```

## Second prompt to Claude Code

After it summarizes correctly, use:

```text
Start with Task 1 only: refactor ysp-site-maintenance.yml by moving the embedded Python logic into scripts/ysp_site_maintenance.py. Do not change lesson content. Do not redesign the site. Show me the planned files before editing.
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
Commit.
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
```

## Recommended First Engineering Milestone

Complete these files:

```text
scripts/ysp_site_maintenance.py
js/ysp-global-nav.js
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
scripts/ysp_validate_site.py
```

Then proceed to content production:

```text
L01 Free Preview Lesson
L01 Full Practice Pack
```
