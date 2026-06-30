# YSP Image Workflow and Asset Checklist

_Last updated: 2026-06-30_

## Purpose

This document defines the safe image workflow for lesson images, gallery assets, and future auto-sort logic.

Image workflow must not be implemented before lesson registry and source-data rules are clear.

## Core Rule

Images are additions, not replacements.

Original lesson text must remain visible.

## Course-Level Asset Folders

Use only course-level asset folders:

```text
lessons/ca-life/assets/pronunciation/
lessons/ca-life/assets/phrases/
lessons/ca-life/assets/dialogues/
lessons/ca-life/assets/speaking/
lessons/ca-life/assets/culture/
```

Equivalent folders may exist under:

```text
lessons/travel/assets/
lessons/business/assets/
```

Do not create per-lesson asset folders.

## Naming Rules

Each lesson must have a registered image prefix:

```text
l01
l02
l03
```

Examples:

```text
l02-pronunciation-1.png
l02-phrases.png
l02-speaking-questions.png
l02-culture-1.png
l02-culture-2.png
l02-d01-model.png
l02-d01-practice.png
```

Dialogue images must use per-dialogue prefix:

```text
l02-d01-
l02-d02-
l02-d03-
l02-d04-
l02-d05-
```

## Future Image Inbox

Recommended future inbox:

```text
image-inbox/
  ca-life-l02-pronunciation-1.png
  ca-life-l02-d01-model.png
  ca-life-l02-d01-practice.png
```

Auto-sort should not guess destinations.

It must read:

```text
docs/YSP_LESSON_REGISTRY.md
lesson-data metadata
```

## Validation Checklist

Before publishing image changes:

```text
[ ] Image prefix exists in registry.
[ ] Image filenames match approved pattern.
[ ] Images are placed in course-level assets folders.
[ ] HTML uses relative paths only.
[ ] Missing images do not break layout.
[ ] No full GitHub Pages image URLs are used.
[ ] No absolute `/assets/` paths are used.
[ ] Site validator passes.
```

## Current Status

```text
Image workflow checklist complete.
Auto-sort implementation not started.
```
