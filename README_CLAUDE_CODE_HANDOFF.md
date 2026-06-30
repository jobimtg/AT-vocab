# YSP AI Handoff — ChatGPT + Local Codex Workflow

_Last checked: 2026-06-30_

## Current Decision

Claude GitHub Action / `@claude` Issue automation is paused.

Reason:

```text
Claude GitHub App was installed.
ANTHROPIC_API_KEY was detected.
OIDC permission was fixed.
The workflow could start.
But the API call failed with: Credit balance is too low.
```

The project will not add Anthropic API credit now.

Current working setup:

```text
ChatGPT GitHub connector = remote repo inspection, branches, PRs, and small safe edits
Local Codex = local repo edits, script refactors, validation, and commits
Claude GitHub Action = paused
```

## Local Repo Path

Use this path on the user's Windows computer:

```text
C:\Users\rose_\Desktop\Claude Skills\GitHub\AT-vocab
```

## Files in This Handoff Package

```text
CLAUDE.md
README_CLAUDE_CODE_HANDOFF.md
docs/YSP_PROJECT_STATUS.md
docs/YSP_SITE_RULES.md
docs/YSP_WORKFLOW_PLAN.md
docs/YSP_CLAUDE_CODE_TASKS.md
```

## Where They Live

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

Current confirmed files:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
.github/workflows/claude-code.yml
scripts/ysp_site_maintenance.py
scripts/ysp_validate_site.py
js/ysp-global-nav.js
```

Important note:

```text
.github/workflows/claude-code.yml may still exist, but @claude automation should not be used unless Anthropic API billing is re-enabled later.
```

Current next focus:

```text
1. Use local Codex to clean duplicate managed lesson-card placement.
2. Run maintenance idempotency test locally.
3. Update progress dashboard checks.
4. Connect validation script to maintenance workflow after confirming validation status.
5. Add a GitHub Issue template for ChatGPT / Codex-safe tasks.
```

## Start Local Codex

In PowerShell:

```powershell
cd "C:\Users\rose_\Desktop\Claude Skills\GitHub\AT-vocab"
git pull origin main
git checkout -b codex/<task-name>
codex
```

Example:

```powershell
cd "C:\Users\rose_\Desktop\Claude Skills\GitHub\AT-vocab"
git pull origin main
git checkout -b codex/fix-duplicate-managed-sections
codex
```

## First Prompt to Local Codex

Use this first:

```text
Read these files first:
- CLAUDE.md
- docs/YSP_PROJECT_STATUS.md
- docs/YSP_WORKFLOW_PLAN.md
- docs/YSP_CLAUDE_CODE_TASKS.md
- docs/YSP_SITE_RULES.md
- README_CLAUDE_CODE_HANDOFF.md

Do not edit anything yet.
Summarize:
1. Current project state
2. Current engineering risks
3. First safe task
4. Files that must not be changed
```

## Safe Working Rule

Do not ask Codex to fix everything at once.

Use this pattern:

```text
Read first.
Summarize first.
Plan first.
Edit one task.
Validate locally.
Show diff.
Commit only after approval.
Push branch.
Open PR.
Move to next task.
```

## Do Not Let Any AI Tool Do This

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

## Standard Codex Task Prompt

```text
Read these files first:
- CLAUDE.md
- docs/YSP_PROJECT_STATUS.md
- docs/YSP_WORKFLOW_PLAN.md
- docs/YSP_CLAUDE_CODE_TASKS.md
- docs/YSP_SITE_RULES.md
- README_CLAUDE_CODE_HANDOFF.md

Task:
<one clear task only>

Allowed files to modify:
- <file 1>
- <file 2>

Do not change:
- lesson content
- public lesson text
- vocabulary text
- dialogue text
- speaking questions
- culture text
- unrelated workflows

Before editing, summarize:
1. Files you will modify
2. Why those files need modification
3. What will not be changed
4. How you will verify the result

After editing:
1. Show changed files
2. Show validation result
3. Do not push until I approve
```

## Recommended First Local Codex Task

```text
Task:
Fix the duplicate auto-managed Featured Lessons / Lesson Library sections appearing after the footer on homepage and lessons page.

Allowed files:
- scripts/ysp_site_maintenance.py
- index.html
- lessons/index.html

Do not change:
- lesson content
- vocabulary text
- dialogue text
- speaking questions
- culture text
- unrelated workflows

Verification:
- Run python scripts/ysp_site_maintenance.py twice.
- Confirm the second run creates no changes.
- Run python scripts/ysp_validate_site.py if possible.
- Show git diff before committing.
```

## Local Verification Commands

```powershell
git status
git diff
python scripts/ysp_validate_site.py
```

For maintenance logic changes:

```powershell
python scripts/ysp_site_maintenance.py
git status
python scripts/ysp_site_maintenance.py
git status
```

Expected result:

```text
First run may update managed sections.
Second run should not create new duplicate changes.
```

## Commit and Push After Approval

```powershell
git add <changed-files>
git commit -m "<clear message>"
git push -u origin codex/<task-name>
```

Then open a PR on GitHub.

## Recommended Next Engineering Milestone

Complete these tasks in order:

```text
1. Clean duplicate managed card placement in `index.html` and `lessons/index.html`.
2. Run maintenance twice and confirm the second run creates no changes.
3. Update `.github/workflows/ysp-progress-dashboard.yml` for current checks.
4. Update `.github/workflows/ysp-site-maintenance.yml` to run `scripts/ysp_validate_site.py` after validation status is known.
5. Add `.github/ISSUE_TEMPLATE/ysp-ai-task.yml` for ChatGPT / Codex tasks.
```

Then proceed to content production:

```text
L01 Free Preview Lesson
L01 Full Practice Pack
Student testing
Purchase or contact pathway
```
