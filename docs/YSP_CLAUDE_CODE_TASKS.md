# YSP AI / Codex Task List

_Last checked: 2026-06-30_

## Current AI Tool Decision

Claude GitHub Action was tested, but it is paused because the Anthropic API account returned:

```text
Credit balance is too low
```

The project will not add Anthropic API credit now.

Current tool strategy:

```text
ChatGPT GitHub connector = remote repo inspection, safe branches, PRs, small edits
Local Codex = larger local edits, script refactors, validation, and controlled commits
Claude GitHub Action = paused
```

Local Codex repo path:

```text
C:\Users\rose_\Desktop\Claude Skills\GitHub\AT-vocab
```

## Important Working Rule

Do one task at a time.

Before editing, ChatGPT or Codex should show:

```text
Files to modify
Why they need modification
What will not be changed
How to verify the result
```

No AI tool should rewrite lesson content unless the user explicitly asks.

## Current Task Status

| Task | Status | Preferred tool | Notes |
|---|---:|---|---|
| Task 1 — Refactor Site Maintenance | Done | Already completed | Workflow now calls `scripts/ysp_site_maintenance.py`. |
| Task 2 — Verify or Create Global Nav JS | Done / needs validation | Codex local | `js/ysp-global-nav.js` exists. Validate behavior on lesson pages. |
| Task 3 — Pronunciation Image Logic | Partial | Codex local | Some lesson pages use image logic; full automation should be improved later. |
| Task 4 — Update Progress Dashboard | Not done | ChatGPT / Codex | Dashboard still needs current-architecture checks. |
| Task 5 — Add Validation Script | Done / needs workflow integration | ChatGPT / Codex | `scripts/ysp_validate_site.py` exists. Add workflow step later. |
| Task 6 — Add or Confirm Site Rules | Done | Already completed | `docs/YSP_SITE_RULES.md` exists. |
| Task 7 — Idempotency Test | Not done | Codex local | Run maintenance twice and confirm second run has no changes. |
| Task 8 — Content Product Step | Not started | Later | Wait until engineering is stable. |
| Task 9 — Claude Code GitHub Action | Paused | Not recommended | Setup worked, but Anthropic API credit is insufficient. |
| Task 10 — Add YSP AI Issue Template | Not done | ChatGPT | Create a template for ChatGPT/Codex-safe tasks. |
| Task 11 — Clean Duplicate Managed Sections | Not done | Codex local preferred | Fix extra homepage / lessons-page managed card sections. |

---

## Standard Local Codex Start Command

In PowerShell:

```powershell
cd "C:\Users\rose_\Desktop\Claude Skills\GitHub\AT-vocab"
git pull origin main
git checkout -b codex/<task-name>
codex
```

Use a clear branch name, for example:

```powershell
git checkout -b codex/fix-duplicate-managed-sections
```

## Standard Local Codex Prompt

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
- vocabulary text
- dialogue text
- speaking questions
- culture text
- brand wording unless explicitly requested
- unrelated workflows

Before editing, summarize:
1. Files you will modify
2. Why they need modification
3. What will not be changed
4. How you will verify

After editing:
1. Show changed files
2. Show validation result
3. Do not push until I approve
```

## Standard Local Verification Commands

```powershell
git status
git diff
python scripts/ysp_validate_site.py
```

If the task changes site maintenance logic, also run:

```powershell
python scripts/ysp_site_maintenance.py
git status
python scripts/ysp_site_maintenance.py
git status
```

Expected result:

```text
First run may update generated sections.
Second run should not create new duplicate changes.
```

## Standard Commit / PR Commands

After reviewing the diff:

```powershell
git add <changed-files>
git commit -m "<clear message>"
git push -u origin codex/<task-name>
```

Then open a pull request on GitHub.

---

## Task 1 — Refactor Site Maintenance

Status:

```text
Done
```

Goal:

```text
Move embedded Python from `.github/workflows/ysp-site-maintenance.yml` into `scripts/ysp_site_maintenance.py`.
```

Files:

```text
.github/workflows/ysp-site-maintenance.yml
scripts/ysp_site_maintenance.py
```

Current note:

```text
Do not repeat this task unless the workflow is accidentally changed again.
```

---

## Task 2 — Verify Global Nav JS

Status:

```text
Done / needs visual validation
```

Goal:

```text
Ensure `js/ysp-global-nav.js` renders stable lesson navigation.
```

Acceptance criteria:

```text
One header only.
One Back to Lessons only.
One Top button only.
Works from lesson pages under ca-life, travel, and business.
Does not break internal sticky lesson tabs.
```

Next action:

```text
Run validation and manually check one lesson per course.
```

---

## Task 3 — Pronunciation Image Logic

Status:

```text
Partial
```

Goal:

```text
Display pronunciation images when matching image files exist.
```

Rules:

```text
u1-l1.html → assets/pronunciation/l01-pronunciation-1.png
u1-l2.html → assets/pronunciation/l02-pronunciation-1.png
```

Acceptance criteria:

```text
Image appears below Pronunciation Spotlight heading.
Button-only placeholder is removed.
No broken image appears when file is missing.
Internal production notes are removed.
```

Current note:

```text
Do not force a single image system across all lessons yet.
First stabilize validation and workflow behavior.
```

---

## Task 4 — Update Progress Dashboard

Status:

```text
Not done
```

Goal:

```text
Update `.github/workflows/ysp-progress-dashboard.yml` to reflect the current architecture and the ChatGPT + local Codex workflow.
```

Remove checks for obsolete workflow names.

Add checks for:

```text
ysp-site-maintenance.yml
ysp-progress-dashboard.yml
js/ysp-global-nav.js
scripts/ysp_site_maintenance.py
scripts/ysp_validate_site.py
CLAUDE.md
docs/YSP_SITE_RULES.md
```

Acceptance criteria:

```text
Dashboard does not modify files.
Dashboard shows useful current status.
Dashboard no longer treats removed old workflows as missing requirements.
Dashboard clearly shows next action.
```

---

## Task 5 — Add Validation Script to Maintenance Workflow

Status:

```text
Script done / workflow integration not done
```

Goal:

```text
Run `scripts/ysp_validate_site.py` from `.github/workflows/ysp-site-maintenance.yml`.
```

Warning:

```text
Before making validation blocking, confirm the current repo passes validation.
If it does not pass, first run it in report-only mode.
```

---

## Task 6 — Site Rules

Status:

```text
Done
```

Current note:

```text
Site rules exist and include folder structure, relative path rules, image naming rules, and Dynamic Image Gallery v3 rules.
```

---

## Task 7 — Idempotency Test

Status:

```text
Not done
```

Goal:

```text
Run maintenance twice.
```

Expected result:

```text
First run may change files.
Second run should produce no changes.
```

Acceptance criteria:

```text
No repeated duplicate blocks.
No repeated card insertion.
No repeated nav loader insertion.
No changing lesson content.
```

---

## Task 8 — Content Product Step After Engineering Is Stable

Status:

```text
Not started
```

Only after engineering is stable:

```text
Convert L01 into a Free Preview Lesson model.
Create L01 Full Practice Pack.
Test with current students.
```

Do not start this before Tasks 4, 7, 10, and 11 are complete.

---

## Task 9 — Claude Code GitHub Action

Status:

```text
Paused
```

Result from testing:

```text
GitHub App installed.
ANTHROPIC_API_KEY detected.
OIDC permission fixed.
Workflow can start.
Claude API call fails because credit balance is too low.
```

Decision:

```text
Do not use @claude Issue automation now.
Do not add Anthropic API credit.
Use ChatGPT GitHub connector and local Codex instead.
```

---

## Task 10 — Add YSP AI Issue Template

Status:

```text
Not done
```

Goal:

```text
Create a reusable GitHub Issue form for ChatGPT / Codex website tasks.
```

Files:

```text
.github/ISSUE_TEMPLATE/ysp-ai-task.yml
```

The issue template should ask for:

```text
Task type
Files allowed to modify
Files not allowed to modify
Content preservation rules
Validation steps
Expected PR summary
```

---

## Task 11 — Clean Duplicate Managed Sections

Status:

```text
Not done
```

Goal:

```text
Fix the extra auto-managed Featured Lessons / Lesson Library sections appearing after the footer on homepage and lessons page.
```

Preferred tool:

```text
Local Codex
```

Allowed files:

```text
scripts/ysp_site_maintenance.py
index.html
lessons/index.html
```

Do not change:

```text
lesson content
vocabulary/dialogue/speaking/culture text
brand wording unless required
course descriptions unless required
```
