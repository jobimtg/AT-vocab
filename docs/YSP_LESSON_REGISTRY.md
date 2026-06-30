# YSP Lesson Registry

_Last updated: 2026-06-30_

## Purpose

This registry is the official tracking table for YSP Learn & Shine lesson files, source data, image prefixes, status, and production notes.

It prevents lesson production from drifting across filenames, paths, image prefixes, course counts, and publication status.

## Registry Rule

Every lesson must be registered before it is generated, refactored, or expanded.

A lesson registry row must exist before:

```text
creating lesson-data JSON
creating or updating lesson HTML
adding images
building Practice Packs
publishing a free preview lesson
```

## Source-of-Truth Decision

Lesson content should not be authored directly as HTML.

Current production direction:

```text
lesson-data JSON / Markdown source
        ↓
fixed L02 renderer / template
        ↓
generated lesson HTML
        ↓
GitHub Pages
```

HTML is the public website output, not the primary editing source.

## Status Labels

Use only these status labels:

| Status | Meaning |
|---|---|
| `published` | Public lesson exists and is usable on the website |
| `golden-reference` | Approved reference for template or data architecture |
| `active-preview` | Public preview lesson exists, but not yet fully converted to data-source workflow |
| `needs-refactor` | Existing lesson works or displays, but should not be used as a production template |
| `planned` | Lesson is planned but not created |
| `data-draft` | JSON / source-data draft exists but HTML is not generated yet |
| `generated-draft` | HTML was generated but not approved for publish |
| `ready-for-review` | Lesson is ready for technical + ESL review |
| `approved` | Lesson passed technical and Senior ESL review |
| `practice-pack-planned` | Public preview exists; paid practice pack not created yet |

## Course Codes

| Course Folder | Course ID | Course Name | CEFR | Core Count | Extended Count |
|---|---|---|---|---:|---:|
| `ca-life` | `canada-en` | Canada Life & Career English | A2→B1 | 25 A2 / 30 B1 | 30 |
| `travel` | `travel-en` | Travel English | A1 | 15 | 30 |
| `business` | `biz-en` | Business English | B2 | 40 | 30 |

## Current Lesson Registry

| Course | Course ID | Unit | Lesson | Public Title | CEFR | HTML Path | Source Data Path | Image Prefix | Status | Notes |
|---|---|---:|---:|---|---|---|---|---|---|---|
| Canada Life & Career English | `canada-en` | 1 | 1 | Welcome to Canada 歡迎來到加拿大 | A2 | `lessons/ca-life/u1-l1.html` | `lesson-data/ca-life/u1-l1.json` | `l01` | `active-preview` | Existing public lesson. Uses image-based sections for phrases, pronunciation, dialogues, speaking, and culture. Must not be used as final Golden template without audit. |
| Canada Life & Career English | `canada-en` | 1 | 2 | Transportation in Canada 加拿大交通 | A2 | `lessons/ca-life/u1-l2.html` | `lesson-data/ca-life/u1-l2.json` | `l02` | `golden-reference` | Uploaded L02 HTML is the current Golden Template reference. Needs to be added to repo as template / source-data proof of concept before mass lesson production. |
| Travel English | `travel-en` | 1 | 1 | Travel English Preview / Airport or Intro Lesson | A1 | `lessons/travel/u1-l1.html` | `lesson-data/travel/u1-l1.json` | `l01` | `active-preview` | Existing public lesson. Useful as content reference, but older structure should not drive future generated lessons. |
| Business English | `biz-en` | 1 | 1 | Business English Preview / Reception or Intro Lesson | B2 | `lessons/business/u1-l1.html` | `lesson-data/business/u1-l1.json` | `l01` | `needs-refactor` | Existing file uses iframe/base64 viewer structure. Do not generate new Business lessons from this structure. |

## Planned Lesson Candidates

Do not generate these until source-data architecture and builder proof of concept are ready.

| Priority | Course | Unit | Lesson | Working Title | CEFR | Planned HTML Path | Planned Source Data Path | Image Prefix | Status | Notes |
|---:|---|---:|---:|---|---|---|---|---|---|---|
| 1 | Canada Life & Career English | 1 | 3 | Phone Plans & Internet 手機與網路 | A2 | `lessons/ca-life/u1-l3.html` | `lesson-data/ca-life/u1-l3.json` | `l03` | `planned` | v3.7 correction standard exists. Must use Golden L02 architecture. |
| 2 | Travel English | 1 | 2 | Airport Check-in / Transportation Travel Lesson | A1 | `lessons/travel/u1-l2.html` | `lesson-data/travel/u1-l2.json` | `l02` | `planned` | Good candidate after L02 JSON proof of concept. |
| 3 | Canada Life & Career English | 1 | 4 | Banking / SIN / Phone Setup | A2 | `lessons/ca-life/u1-l4.html` | `lesson-data/ca-life/u1-l4.json` | `l04` | `planned` | Align with Canada life setup pathway. |
| 4 | Business English | 1 | 1 | Business L01 Clean Refactor | B2 | `lessons/business/u1-l1.html` | `lesson-data/business/u1-l1.json` | `l01` | `planned` | Refactor plan required before editing existing public file. |

## Image Prefix Rules

Each lesson must use one lesson-level prefix:

```text
l01
l02
l03
```

Image filename examples:

```text
l02-pronunciation-1.png
l02-phrases.png
l02-speaking-questions.png
l02-culture-1.png
l02-culture-2.png
l02-d01-model.png
l02-d01-practice.png
l02-d02-model.png
l02-d02-practice.png
```

Dialogue images must use per-dialogue prefixes:

```text
l02-d01-
l02-d02-
l02-d03-
l02-d04-
l02-d05-
```

Do not use broad dialogue prefixes like:

```text
l02-d-
l02-dialogue-
```

## Asset Folder Rules

Use course-level asset folders only:

```text
lessons/ca-life/assets/pronunciation/
lessons/ca-life/assets/phrases/
lessons/ca-life/assets/dialogues/
lessons/ca-life/assets/speaking/
lessons/ca-life/assets/culture/
```

Do not create per-lesson asset folders:

```text
lessons/ca-life/u1-l2/assets/
lessons/travel/u1-l2/assets/
lessons/business/u1-l1/assets/
```

## Required Pre-Production Checklist

Before creating a new lesson:

```text
[ ] Registry row exists.
[ ] Course ID is correct.
[ ] CEFR is correct.
[ ] Source data path is reserved.
[ ] HTML output path is reserved.
[ ] Image prefix is reserved.
[ ] Golden L02 template rules are loaded.
[ ] Senior ESL Reviewer gate is planned.
[ ] Previously Learned source is known or placeholder rule is used.
```

## Required Pre-Publish Checklist

Before publishing a lesson:

```text
[ ] JSON / source data validates.
[ ] Generated HTML validates.
[ ] 10-tab order passes.
[ ] Core count matches CEFR.
[ ] Extended count is 30.
[ ] Phrases count is 5.
[ ] Dialogues count is 5.
[ ] Speaking count is 5.
[ ] Culture count is 2.
[ ] PRON exists.
[ ] No forbidden legacy classes.
[ ] No duplicate nav / Top button.
[ ] Site validator passes.
[ ] Senior ESL Reviewer gate passes.
```

## Paid Product Relationship

The registry also controls future product planning.

Public lessons may later connect to:

```text
Free Preview Lesson
Full Practice Pack
Guided Trial Lesson
Practice Pack Bundle
```

Do not create Practice Packs until the lesson has a registry row and a stable public preview structure.

## Next Step

Create a proof-of-concept source data file from L02:

```text
lesson-data/ca-life/u1-l2.json
```

Then create or store the fixed template:

```text
templates/lesson-l02-template.html
```

After that, build and validate the first generated HTML output.
