# CLAUDE.md — YSP Learn & Shine / AT-vocab

@AGENTS.md

> Shared YSP Agent Loop, Reviewer, validator, Git/Notion completion rules are maintained in `AGENTS.md`. The Claude-specific website guidance below remains additive and must not override newer dated YSP rules fetched from Notion.

## Role

You are maintaining the GitHub Pages repository for the YSP Learn & Shine English-learning website.

Repository:

```text
jobimtg/AT-vocab
```

Website:

```text
https://jobimtg.github.io/AT-vocab/
```

Brand:

```text
YSP Learn & Shine
```

Slogan:

```text
Learn with Purpose. Shine with Confidence.
```

## Main Goal

Keep this site low-maintenance, clean, stable, and safe for a non-engineer user.

The website is not a full free course database. It is a public brand entrance and preview lesson library that supports:

```text
Free Preview Lessons
Full Practice Packs
Guided Trial Lessons
```

## Highest-Priority Rules

Do not rewrite lesson content unless the user explicitly asks.

Do not redesign the whole site unless the user explicitly asks.

Do not restore old patch workflows.

Do not add report folders.

Do not create new workflows unless truly necessary.

Do not insert internal production notes into public HTML pages.

Do not remove original learning sections from lesson pages.

Do not break GitHub Pages relative paths.

Do not add duplicate header, duplicate Back to Lessons, or duplicate Top button.

## Current Active Workflows

Only these workflows should remain active:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

Old workflows should not be restored.

## Current Architecture Direction

The final stable architecture should be:

```text
.github/workflows/ysp-site-maintenance.yml
    ↓ calls
scripts/ysp_site_maintenance.py

.github/workflows/ysp-progress-dashboard.yml
    ↓ display-only progress summary

js/ysp-global-nav.js
    ↓ renders global navigation on lesson pages
```

## Required Maintenance Behavior

The maintenance process must be idempotent.

Running the maintenance workflow twice should result in:

```text
First run: apply needed fixes
Second run: no changes to commit
```

## Lesson Page Requirements

Every lesson page should have:

```text
YSP Learn & Shine brand navigation
Home link
Lessons link
About link
Back to Lessons button
One Top button only
Original lesson learning content preserved
```

## Pronunciation Image Rule

For a lesson such as:

```text
lessons/ca-life/u1-l1.html
```

The pronunciation image should be detected from:

```text
lessons/ca-life/assets/pronunciation/l01-pronunciation-1.png
```

For:

```text
lessons/ca-life/u1-l2.html
```

Use:

```text
lessons/ca-life/assets/pronunciation/l02-pronunciation-1.png
```

Same pattern applies under:

```text
lessons/travel/assets/pronunciation/
lessons/business/assets/pronunciation/
```

If the image exists, display it as an image under the Pronunciation Spotlight heading.

If it does not exist, do not create a broken image.

## Internal Notes to Remove from Public HTML

Remove visible public text containing:

```text
本分頁使用
請將圖片放在
完整發音教學圖
assets/pronunciation
```

But do not remove valid `src="assets/pronunciation/..."` image paths.

## Before Editing

Before editing, summarize:

```text
1. What files you will modify
2. Why those files need modification
3. What will not be changed
4. How you will verify the result
```

## After Editing

After editing, verify:

```text
No duplicate header
No duplicate Back to Lessons
No duplicate Top button
No internal production notes
Pronunciation image displays when image exists
lessons/index.html cards are correct
index.html featured lesson cards are correct
Workflow can run twice without repeated changes
```
