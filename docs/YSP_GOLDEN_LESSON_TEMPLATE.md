# YSP Golden Lesson Template

_Last updated: 2026-06-30_

## Purpose

This document defines the Phase 2 lesson-production standard for YSP Learn & Shine.

It combines two required layers:

```text
1. Technical Golden Template
   HTML structure, tab order, data schema, class names, card layout, validation.

2. Senior ESL Reviewer Gate
   Teaching feasibility, timing, cognitive load, speaking output, pronunciation, review, assessment.
```

No new lesson HTML should be generated or merged until it follows this document, or until the user explicitly approves an exception.

## Golden Master

The intended golden master is:

```text
L02 — Transportation in Canada 加拿大交通
```

Every future lesson should reuse the same architecture as the L02 Golden Template:

```text
single-file HTML
zh-Hant bilingual lesson style
YSP Learn & Shine brand header/footer
10-tab order
short class-name system
data-driven renderer
Core / Extended / Phrases / Dialogues / Speaking / Culture / Pronunciation data arrays
familiarity buttons
progress system
```

If the exact L02 source file is not present in the repository, this document and the uploaded v3.7 skill are the working source of truth until L02 is added.

## Current Repository Audit

| Course | File | Current Status | Template Decision |
|---|---|---:|---|
| Canada Life & Career | `lessons/ca-life/u1-l1.html` | Modern tab/data-driven direction | Current closest clean reference, but not final until compared with L02 |
| Travel English | `lessons/travel/u1-l1.html` | Older anchor navigation style | Content reference only; not final structure |
| Business English | `lessons/business/u1-l1.html` | iframe/base64 viewer | Not acceptable as a future lesson template |

## Required 10-Tab Order

Every generated lesson HTML must use exactly this tab order:

| Index | Tab Label | Purpose |
|---:|---|---|
| 1 | 📊 總覽 | Stats panel and progress |
| 2 | 📚 Core | Core flashcards |
| 3 | 📖 Extended | Extended reference vocabulary |
| 4 | 🔁 Drilling | Three-level drilling |
| 5 | 💬 Phrases | Useful phrases |
| 6 | 🎯 發音 | Pronunciation spotlight |
| 7 | 🎭 Dialogues | Role-play dialogues |
| 8 | 🗣️ Speaking | Speaking questions |
| 9 | 🌍 Culture | Culture topics |
| 10 | 📋 進度 | Previously Learned and current progress |

Do not create separate tabs such as:

```text
Culture & Warmup
Spiral Review
Practice
```

## Required Data Variables

Every generated lesson HTML must include these variables before the renderer script:

```javascript
var CATS = [];
var V = [];
var EXT = [];
var PHRASES = [];
var DIALOGUES = [];
var SPEAKING = [];
var CULTURE = [];
var PRON = {};
```

The data script must appear before the renderer script.

## Course Counts

| Course | CEFR | Core | Extended | Phrases | Dialogues | Speaking | Culture | Pronunciation |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Travel English | A1 | 15 | 30 | 5 | 5 | 5 | 2 | 1 |
| Canada Life & Career English | A2 | 25 | 30 | 5 | 5 | 5 | 2 | 1 |
| Canada Life & Career English | B1 | 30 | 30 | 5 | 5 | 5 | 2 | 1 |
| Business English | B2 | 40 | 30 | 5 | 5 | 5 | 2 | 1 |

Under-producing or over-producing these counts is a critical failure unless the user explicitly approves a special lesson type.

## Required Short Class Names

Generated lesson HTML must use the L02 short class-name system.

| Concept | Required Class |
|---|---|
| Tabs container | `.tabs` |
| Tab button | `.tb` |
| Tab panel | `.tpn` |
| Core grid | `.cg` |
| Core card | `.vc` |
| Front | `.vf` |
| Back | `.vb` |
| Flipped state | `.fl` |
| English front | `.ew` |
| English back | `.eb` |
| Chinese back | `.zb` |
| Meaning | `.mg` |
| Example | `.ex` |
| Practice item | `.pi` |
| Familiarity bar | `.famb` |
| Familiarity button | `.fm` |
| Extended grid | `.eg` |
| Extended card | `.ec` |

## Forbidden Legacy Patterns

If any of these appear in generated lesson HTML, the lesson is invalid:

```text
.vocab-card
.vocab-word
.vocab-phonetic
.vocab-meaning
.vocab-chinese
.vocab-example
.vocab-grid
.tab-container
.tab-btn
.tab-content
flipped
vcard-front
vcard-back
vcard-en-front
vcard-en-back
```

Exception: these strings may appear only in documentation files.

## Core Card Visual Rules

Every Core card must match the L02 visual model.

Front:

```text
small SVG icon at top
pronunciation below icon
English word large and readable
flip hint
```

Back:

```text
English word
Traditional Chinese
2 meaning sentences
2 example sentences
practice label
2 practice blank sentences
familiarity buttons
```

Required flip system:

```css
.vb { display:none; }
.vc.fl .vf { display:none; }
.vc.fl .vb { display:block; }
```

Do not use CSS 3D flip, perspective, transform-style, backface-visibility, or absolute-positioned card faces.

## Data Schema Rules

### Core `V[]`

Each Core item must include:

```text
en
zh
pr
cat
m1
m2
e1
e2
p1
p2
svg
```

Rules:

```text
cat must be 0–4
m1/m2 = exactly 2 short meaning sentences
e1/e2 = exactly 2 examples
p1/p2 = exactly 2 practice sentences with one blank each
svg is required for every Core card
```

### Extended `EXT[]`

Each Extended item must include:

```text
en
zh
pr
cat
m
ex
```

Extended vocabulary is self-study/reference only. It should not include practice blanks.

### Phrases

Exactly 5 phrases:

```text
first 3 = core
last 2 = extended
```

### Dialogues

Exactly 5 dialogues:

```text
first 3 = required
last 2 = choice / extension
Dialogue 3 must include a problem or complication
Every dialogue must include a Now you try prompt
```

### Speaking

Exactly 5 questions:

```text
Tier 1 = 2 questions
Tier 2 = 2 questions
Tier 3 = 1 question
```

### Culture

Exactly 2 culture items:

```text
1 warm-up
1 closing
Each has 3 discussion questions
```

### Pronunciation

Exactly 1 pronunciation spotlight:

```text
3–5 practice words
1 full practice sentence
clear oral target
```

## Previously Learned Rule

Previously Learned must never be guessed.

Valid sources:

```text
existing prior lesson HTML files
Notion tracker
user-provided vocabulary tracker
prior generated files in the same session
```

If the source is unavailable, write:

```text
Previously Learned data source unavailable. I will leave the section as a placeholder rather than inventing prior vocabulary.
```

## Senior ESL Reviewer Gate

A technically valid lesson can still fail if it is not teachable.

Every lesson must be reviewed across these 10 dimensions:

| Dimension | Passing Standard |
|---|---|
| Topic Coverage & Relevance | Solves a real student need |
| Timing Feasibility | Fits realistic online class time |
| Cognitive Load & Vocabulary Strategy | Active load matches CEFR and lesson length |
| Spiral Review & Retention | Prior content is recycled in context |
| Speaking & Pronunciation | Student speaks 60–70%; pronunciation is explicit |
| Error Correction Strategy | Immediate and delayed correction are planned |
| Assessment & Progress Tracking | Student can see progress |
| Student Autonomy & Differentiation | Student has choices and personalization |
| Cultural Content Integration | Culture is practical and not easily skipped |
| Production Feasibility | Lesson can be produced repeatedly |

Minimum approval target:

```text
No Critical issues
Average review score: 7/10 or higher
Timing Feasibility: 8/10 or higher
Cognitive Load: 8/10 or higher
Speaking & Pronunciation: 8/10 or higher
```

## 50-Minute Online Lesson Timing Gate

Real online 1-on-1 teaching time is usually:

```text
43–45 minutes
```

because time is lost to greeting, setup, questions, and occasional tech issues.

A safe lesson timing model:

| Section | Time |
|---|---:|
| Greeting / goal check | 2–3 min |
| Overview / warm-up | 3–4 min |
| Core vocabulary | 12–15 min |
| Drilling / pronunciation | 6–8 min |
| Useful phrases | 5–7 min |
| Dialogue practice | 8–12 min |
| Speaking questions | 5–8 min |
| Culture / wrap-up | 3–5 min |

If a lesson contains all content in full, the teacher must choose a live-class focus and leave some material as reference.

## Vocabulary Load Teaching Rule

Core and Extended must be treated differently:

```text
Core = active in-class teaching
Extended = reference / optional self-study
```

A2 learners usually cannot actively learn 55 new items in one 50-minute class.

Therefore, Canada Life A2 may show:

```text
25 Core + 30 Extended
```

but the live lesson should actively prioritize a subset of Core items based on student needs.

## Error Correction Rule

Every lesson should include:

```text
1 pronunciation correction
1 phrase upgrade
1 confidence note
1 next practice target
```

Correction strategy:

```text
Immediate correction:
- target pronunciation
- key phrase form
- errors that block understanding

Delayed correction:
- fluency task errors
- repeated grammar patterns
- natural phrasing upgrades
```

## Image Gallery Rule

Gallery blocks are additions, not replacements.

Original text must remain visible.

The gallery updater may only replace content inside:

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START -->
...
<!-- YSP_IMAGE_GALLERY_MOUNT_END -->
```

The updater must preserve:

```text
outer section
data-ysp-gallery
data-ysp-image-dir
data-ysp-image-prefix
data-ysp-image-title
data-ysp-image-subtitle
mount markers
```

## Validation Checklist Before Delivery

Before delivering lesson HTML, confirm:

| Check | Required Result |
|---|---|
| Single HTML file | PASS |
| `html lang="zh-Hant"` | PASS |
| 10 tabs exist | PASS |
| Tab order matches Golden Template | PASS |
| `CATS.length === 5` | PASS |
| `V.length` matches CEFR | PASS |
| `EXT.length === 30` | PASS |
| `PHRASES.length === 5` | PASS |
| `DIALOGUES.length === 5` | PASS |
| `SPEAKING.length === 5` | PASS |
| `CULTURE.length === 2` | PASS |
| `PRON` exists | PASS |
| Every Core card has `svg` | PASS |
| Every Core card has `m1,m2,e1,e2,p1,p2` | PASS |
| No forbidden legacy classes | PASS |
| Uses `.vc/.vf/.vb` card system | PASS |
| Uses `.famb/.fm` familiarity system | PASS |
| Uses YSP brand header/footer | PASS |
| Previously Learned is real or placeholder | PASS |
| Senior ESL Reviewer gate passed | PASS |

## Phase 2 Decision

Do not use Business L01 as a production template.

Do not generate new lessons from Travel L01's older anchor-navigation structure.

Use the L02 Golden Template standard as the production target. Until the official L02 HTML is in the repo, use this document plus the uploaded v3.7 skill as the working contract.

## Next Step

Create:

```text
docs/YSP_LESSON_REGISTRY.md
```

The registry must connect:

```text
course
unit
lesson
HTML path
CEFR
image prefix
status
notes
```
