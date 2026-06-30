# YSP Phase 2 Content Plan

_Last updated: 2026-06-30_

## Phase 2 Goal

Phase 2 moves the project from website automation foundation into controlled lesson production.

The goal is not to publish many lessons quickly. The goal is to create a repeatable, safe lesson-production system that keeps every lesson visually consistent, technically valid, and aligned with YSP Learn & Shine.

## Phase 1 Completion Gate

Phase 1 is complete.

Confirmed foundation:

```text
Website automation architecture: 100%
Next engineering readiness: 100%
Lesson pages with global loader: 3/3
YSP Site Validator: 0 errors, 0 warnings
YSP Site Maintenance: idempotent, no repeated changes
```

## Current Source of Truth

The current technical source of truth is:

```text
CLAUDE.md
docs/YSP_SITE_RULES.md
docs/YSP_PROJECT_STATUS.md
docs/YSP_WORKFLOW_PLAN.md
docs/YSP_CLAUDE_CODE_TASKS.md
README_CLAUDE_CODE_HANDOFF.md
```

For Phase 2 lesson production, the most important rules are:

```text
Do not rewrite lesson content unless explicitly requested.
Do not remove vocabulary, dialogues, speaking questions, culture notes, or JavaScript lesson data.
Do not replace original text content with image galleries.
Do not create duplicate navigation, Back to Lessons, or Top buttons.
Use course-level assets folders only.
Use relative paths only.
Keep YSP Site Maintenance idempotent.
Run validation after technical changes.
```

## Existing Lesson Inventory

| Course | File | Current Status | Phase 2 Action |
|---|---|---:|---|
| Canada Life & Career | `lessons/ca-life/u1-l1.html` | Active preview lesson | Use as current clean lesson reference after audit |
| Travel English | `lessons/travel/u1-l1.html` | Active preview lesson | Compare against future Travel template standard |
| Business English | `lessons/business/u1-l1.html` | Partial / iframe-base64 structure | Refactor later into clean lesson template |

## Important Phase 2 Decision

Do not start by generating many new lessons.

Start by locking the lesson standard.

Phase 2 should proceed in this order:

```text
Step 2.1 — Golden Lesson Template Audit
Step 2.2 — Lesson Registry
Step 2.3 — Course Production Rules
Step 2.4 — Business L01 Refactor Plan
Step 2.5 — First New Lesson Draft
Step 2.6 — Image Gallery / Asset Checklist
Step 2.7 — Practice Pack Template
```

## Step 2.1 — Golden Lesson Template Audit

Purpose:

```text
Identify the exact HTML structure that future lessons must follow.
```

Audit targets:

```text
lessons/ca-life/u1-l1.html
lessons/travel/u1-l1.html
lessons/business/u1-l1.html
```

Audit checklist:

```text
Tab order
Header structure
Vocabulary card layout
Core / Extended structure
Drilling section
Useful Phrases section
Pronunciation Spotlight section
Dialogue Practice section
Speaking Questions section
Culture section
Review / wrap-up section
Image gallery placement
Relative path usage
Global nav loader
No duplicate Top button
No internal production notes
Validation result
```

Expected output:

```text
docs/YSP_GOLDEN_LESSON_TEMPLATE.md
```

## Step 2.2 — Lesson Registry

Purpose:

```text
Track approved lesson files, course paths, image prefixes, and publish status.
```

Recommended file:

```text
docs/YSP_LESSON_REGISTRY.md
```

Registry fields:

```text
course
unit
lesson
html path
public title
CEFR
image prefix
status
notes
```

Initial rows:

| Course | Unit | Lesson | HTML Path | Image Prefix | Status |
|---|---:|---:|---|---|---:|
| Canada Life & Career | 1 | 1 | `lessons/ca-life/u1-l1.html` | `l01` | published |
| Travel English | 1 | 1 | `lessons/travel/u1-l1.html` | `l01` | published |
| Business English | 1 | 1 | `lessons/business/u1-l1.html` | `l01` | needs refactor |

## Step 2.3 — Course Production Rules

Purpose:

```text
Separate course planning from technical site rules.
```

Recommended file:

```text
docs/YSP_COURSE_PRODUCTION_RULES.md
```

Should include:

```text
Course track definitions
CEFR target per course
Vocabulary count rules
Dialogue count rules
Image requirements
Free Preview vs Full Practice Pack boundaries
What public HTML may show
What belongs only in paid practice packs
```

## Step 2.4 — Business L01 Refactor Plan

Current issue:

```text
Business L01 exists, but it uses an iframe/base64 combined structure.
```

Risk:

```text
Harder to validate
Harder to maintain
Harder to reuse as a clean template
Not aligned with the public lesson-page architecture
```

Action:

```text
Create a refactor plan first.
Do not rewrite it directly until the target template is approved.
```

## Step 2.5 — First New Lesson Draft

Only start after Steps 2.1–2.3 are done.

Recommended first new lesson candidate:

```text
Travel English U1-L2 or Canada Life & Career U1-L2
```

Do not begin Business expansion until Business L01 has a clean template path.

## Step 2.6 — Image Gallery / Asset Checklist

Before adding lesson images, confirm:

```text
Image prefix is registered.
Assets use course-level folders.
No per-lesson asset folders are created.
Gallery prefix includes trailing hyphen.
Dialogue images use per-dialogue prefixes: l01-d01-, l01-d02-, etc.
Images are optional; missing images must not create broken img tags.
```

## Step 2.7 — Practice Pack Template

Do not build the paid/full pack before the public preview lesson structure is stable.

Practice Pack should later include:

```text
Full vocabulary review
Dialogue practice
Speaking drills
Pronunciation review
Answer key
Printable PDF format
Optional student homework version
```

## Phase 2 Safety Rules

Every Phase 2 task must state:

```text
Allowed files
Do-not-change files
Whether lesson content may be edited
Whether only docs are being changed
Validation method
Expected result
```

Every technical change must pass:

```text
YSP Site Maintenance
YSP Site Validator
YSP Progress Dashboard
```

## Phase 2 Current Status

| Step | Task | Status |
|---:|---|---:|
| 2.1 | Golden Lesson Template Audit | In progress |
| 2.2 | Lesson Registry | Not started |
| 2.3 | Course Production Rules | Not started |
| 2.4 | Business L01 Refactor Plan | Not started |
| 2.5 | First New Lesson Draft | Not started |
| 2.6 | Image Gallery / Asset Checklist | Not started |
| 2.7 | Practice Pack Template | Not started |

## Next Action

Create:

```text
docs/YSP_GOLDEN_LESSON_TEMPLATE.md
```

This should document the exact reusable lesson structure before any new lesson is generated.
