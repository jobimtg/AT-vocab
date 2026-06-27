# YSP Site Rules

## Purpose

This document defines the stable rules for the YSP Learn & Shine / AT-vocab website.

The goal is to keep the website easy to update, safe for a non-engineer, and stable when new lesson HTML files are uploaded.

## Folder Structure

Required main folders:

```text
assets/
docs/
js/
lessons/
scripts/
.github/workflows/
```

Lesson folders:

```text
lessons/ca-life/
lessons/travel/
lessons/business/
```

Image folders inside each course folder:

```text
lessons/ca-life/assets/pronunciation/
lessons/travel/assets/pronunciation/
lessons/business/assets/pronunciation/
```

## Lesson Naming Rule

Use this pattern:

```text
u1-l1.html
u1-l2.html
u2-l1.html
```

Examples:

```text
lessons/ca-life/u1-l1.html
lessons/travel/u1-l1.html
lessons/business/u1-l1.html
```

## Pronunciation Image Naming Rule

For lesson file:

```text
u1-l1.html
```

Use image:

```text
l01-pronunciation-1.png
```

For:

```text
u1-l2.html
```

Use:

```text
l02-pronunciation-1.png
```

Full example:

```text
lessons/ca-life/u1-l1.html
lessons/ca-life/assets/pronunciation/l01-pronunciation-1.png
```

## Workflow Rules

Only two workflows should be active:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

Do not restore old workflows such as:

```text
auto-update-lessons-clean-header.yml
clean-homepage-layout.yml
clean-lessons-layout.yml
fix-top-button-overlap.yml
fix-practice-pack-placement.yml
fix-revenue-sections-placement.yml
step1-revenue-positioning.yml
update-ysp-progress-tracker.yml
```

## Maintenance Workflow May Modify

The site maintenance script may modify:

```text
index.html
lessons/index.html
lessons/**/*.html
```

It may add or update:

```text
global nav loader
lesson cards
featured lesson cards
Back to Lessons support
Top button support
pronunciation image display
```

## Maintenance Workflow Must Not Modify

The site maintenance script must not:

```text
rewrite lesson teaching content
remove original learning sections
change lesson text unless removing internal production notes
create report folders
add duplicate generated blocks
restore old patch workflow logic
```

## Public HTML Must Not Contain Internal Notes

Remove visible notes containing:

```text
本分頁使用
請將圖片放在
完整發音教學圖
```

Do not remove valid image paths inside `src` attributes.

## Global Navigation Rule

Every lesson page should load:

```text
js/ysp-global-nav.js
```

Relative path examples:

```text
lessons/ca-life/u1-l1.html
→ ../../js/ysp-global-nav.js
```

The global navigation should render:

```text
YSP Learn & Shine
Home
Lessons
About
Back to Lessons
Top
```

## Idempotency Rule

The maintenance process must be safe to run repeatedly.

Running it twice should not create:

```text
duplicate headers
duplicate Back to Lessons
duplicate Top buttons
duplicate lesson card sections
extra commits when nothing changed
```

## Validation Rule

After major changes, run validation.

Validation should check:

```text
lesson pages have nav loader
no duplicate Top button
no duplicate Back to Lessons
no internal production notes
pronunciation image rules are valid
lesson links are not broken
```
