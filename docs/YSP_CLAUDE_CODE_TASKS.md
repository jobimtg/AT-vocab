# YSP Claude Code Tasks

_Last checked: 2026-06-29_

## Important Working Rule

Do one task at a time.

Before editing, Claude Code should show:

```text
Files to modify
Why they need modification
What will not be changed
How to verify the result
```

Claude Code must not rewrite lesson content unless the user explicitly asks.

## Current Task Status

| Task | Status | Notes |
|---|---:|---|
| Task 1 — Refactor Site Maintenance | Done | Workflow now calls `scripts/ysp_site_maintenance.py`. |
| Task 2 — Verify or Create Global Nav JS | Done / needs validation | `js/ysp-global-nav.js` exists. Validate behavior on lesson pages. |
| Task 3 — Pronunciation Image Logic | Partial | Some lesson pages use image logic; full automation should be improved later. |
| Task 4 — Update Progress Dashboard | Not done | Dashboard still needs current-architecture checks. |
| Task 5 — Add Validation Script | Done / needs workflow integration | `scripts/ysp_validate_site.py` exists. Add workflow step later. |
| Task 6 — Add or Confirm Site Rules | Done | `docs/YSP_SITE_RULES.md` exists. |
| Task 7 — Idempotency Test | Not done | Run maintenance twice and confirm second run has no changes. |
| Task 8 — Content Product Step | Not started | Wait until engineering is stable. |
| Task 9 — Add Claude Code GitHub Action | Not done | Add `.github/workflows/claude-code.yml`. |
| Task 10 — Add YSP AI Issue Template | Not done | Add `.github/ISSUE_TEMPLATE/ysp-ai-task.yml`. |

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

Acceptance criteria:

```text
Workflow YAML is short.
Python logic is in scripts/ysp_site_maintenance.py.
Workflow still runs maintenance.
No lesson content is rewritten.
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
Ensure `js/ysp-global-nav.js` exists and renders stable lesson navigation.
```

Files:

```text
js/ysp-global-nav.js
```

It should render:

```text
Home
Lessons
About
Book a Trial Lesson
Back to Lessons
Top
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
Update `.github/workflows/ysp-progress-dashboard.yml` to reflect the current two-workflow system and current scripts.
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

## Task 5 — Add Validation Script

Status:

```text
Done / needs workflow integration
```

Goal:

```text
Create `scripts/ysp_validate_site.py`.
```

Validation should check:

```text
Every lesson page has global nav loader
No duplicate Top button
No duplicate Back to Lessons
No internal production notes
No obvious broken local image paths
Dynamic image gallery markers and attributes
Pronunciation image naming rules
```

Acceptance criteria:

```text
Readable output.
Clear failure messages.
Can run locally with python3 scripts/ysp_validate_site.py.
```

Next action:

```text
Add it to `.github/workflows/ysp-site-maintenance.yml`.
```

---

## Task 6 — Add or Confirm Site Rules

Status:

```text
Done
```

Goal:

```text
Keep `docs/YSP_SITE_RULES.md` as the source of truth.
```

Acceptance criteria:

```text
Rules match actual workflow behavior.
Rules help prevent future accidental changes.
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

Do not start this before Tasks 4, 7, 9, and 10 are complete.

---

## Task 9 — Add Claude Code GitHub Action

Status:

```text
Not done
```

Goal:

```text
Allow the user to create GitHub Issues and tag @claude so Claude Code can edit the repo and open PRs.
```

Files:

```text
.github/workflows/claude-code.yml
```

Before editing, confirm:

```text
Claude GitHub App is installed.
ANTHROPIC_API_KEY exists in GitHub Actions secrets.
```

Acceptance criteria:

```text
@claude can respond in an issue or PR.
Claude reads CLAUDE.md and docs/YSP_*.md first.
Claude creates PRs instead of pushing directly to main.
Claude does not rewrite lesson content unless explicitly instructed.
```

---

## Task 10 — Add YSP AI Issue Template

Status:

```text
Not done
```

Goal:

```text
Create a reusable GitHub Issue form for YSP website tasks.
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

Acceptance criteria:

```text
Future AI tasks are clear and safe.
User does not need to rewrite long prompts every time.
Claude has enough context to work without guessing.
```
