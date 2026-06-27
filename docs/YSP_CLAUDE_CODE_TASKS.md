# YSP Claude Code Tasks

## Important Working Rule

Do one task at a time.

Before editing, Claude Code should show:

```text
Files to modify
Why they need modification
What will not be changed
How to verify the result
```

## Task 1 — Refactor Site Maintenance

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

## Task 2 — Verify or Create Global Nav JS

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
YSP Learn & Shine
Home
Lessons
About
Back to Lessons
Top
```

Acceptance criteria:

```text
One header only.
One Back to Lessons only.
One Top button only.
Works from lesson pages under ca-life, travel, and business.
```

## Task 3 — Pronunciation Image Logic

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

## Task 4 — Update Progress Dashboard

Goal:

```text
Update `.github/workflows/ysp-progress-dashboard.yml` to reflect the current two-workflow system.
```

Remove checks for obsolete workflow names.

Add checks for:

```text
ysp-site-maintenance.yml
ysp-progress-dashboard.yml
js/ysp-global-nav.js
scripts/ysp_site_maintenance.py
scripts/ysp_validate_site.py
```

Acceptance criteria:

```text
Dashboard does not modify files.
Dashboard shows useful current status.
Dashboard no longer says missing old workflows are problems.
```

## Task 5 — Add Validation Script

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
No obvious broken local links
Pronunciation image naming rules
```

Acceptance criteria:

```text
Readable output.
Clear failure messages.
Can run locally with python3 scripts/ysp_validate_site.py.
```

## Task 6 — Add or Confirm Site Rules

Goal:

```text
Keep `docs/YSP_SITE_RULES.md` as the source of truth.
```

Acceptance criteria:

```text
Rules match actual workflow behavior.
Rules help prevent future accidental changes.
```

## Task 7 — Idempotency Test

Goal:

```text
Run maintenance twice.
```

Expected result:

```text
First run may change files.
Second run should produce no changes.
```

## Task 8 — Content Product Step After Engineering Is Stable

Only after engineering is stable:

```text
Convert L01 into a Free Preview Lesson model.
Create L01 Full Practice Pack.
Test with current students.
```

Do not start this before Tasks 1–7 are complete.
