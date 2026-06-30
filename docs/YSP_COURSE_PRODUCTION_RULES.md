# YSP Course Production Rules

_Last updated: 2026-06-30_

## Purpose

This document separates course-production rules from website-engineering rules.

The website foundation is stable. Future work must now protect teaching quality, product positioning, and repeatable production.

## Core Product Positioning

YSP Learn & Shine should use this public-facing structure:

```text
Free Preview Lessons
Full Practice Packs
Guided Trial Lessons
```

The public website should not become a full free course database.

## Course Tracks

| Course | Course ID | CEFR | Main Student | Public Role |
|---|---|---|---|---|
| Travel English | `travel-en` | A1 | Beginner travelers | Easy entry / free preview / social content |
| Canada Life & Career English | `canada-en` | A2→B1 | WHV, newcomers, adult learners in Canada | Main paid course pathway |
| Business English | `biz-en` | B2 | Workplace / professional learners | Higher-level future product |

## Required Counts

| Course | CEFR | Core | Extended | Phrases | Dialogues | Speaking | Culture | Pronunciation |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Travel English | A1 | 15 | 30 | 5 | 5 | 5 | 2 | 1 |
| Canada Life & Career English | A2 | 25 | 30 | 5 | 5 | 5 | 2 | 1 |
| Canada Life & Career English | B1 | 30 | 30 | 5 | 5 | 5 | 2 | 1 |
| Business English | B2 | 40 | 30 | 5 | 5 | 5 | 2 | 1 |

## Public Lesson vs Paid Practice Pack

| Content Type | Free Preview Lesson | Full Practice Pack |
|---|---:|---:|
| Lesson overview | Yes | Yes |
| Core vocabulary | Partial / selected live focus | Full |
| Extended vocabulary | Visible reference | Full review + exercises |
| Useful phrases | Yes | Extra substitution drills |
| Pronunciation | Yes | Extra practice page |
| Dialogues | Preview / selected | Full model + Now You Try + variations |
| Speaking questions | Preview | Full worksheet / homework |
| Culture | Yes | Extended discussion prompts |
| Answer key | No | Yes |
| Teacher notes | No public notes | Teacher-only optional pack |
| Printable PDF | No or limited | Yes |

## Production Rule

Do not generate many lessons before the data-source workflow is stable.

Safe sequence:

```text
1. Register lesson.
2. Create source-data file.
3. Validate source data.
4. Build generated HTML from Golden L02 renderer.
5. Run site validator.
6. Review with Senior ESL Reviewer.
7. Publish only after checks pass.
```

## Previously Learned Rule

Previously Learned must never be guessed.

Valid sources:

```text
actual previous lesson HTML
lesson-data files
Notion tracker
user-provided tracker
same-session prior generated files
```

## Marketing Boundary

Website lessons should create trust and conversion.

Do not give away the entire paid product for free.

Recommended public CTA:

```text
Try the free preview lesson.
Download the full practice pack.
Book a guided trial lesson.
```
