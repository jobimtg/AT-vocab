# YSP First New Lesson Draft Plan

_Last updated: 2026-06-30_

## Purpose

This document defines the first safe new-lesson draft path after the Phase 2 foundation.

The goal is not to publish a new lesson immediately. The goal is to choose the safest first draft after the Golden L02 source-data proof is stable.

## Decision

Do not generate new HTML directly.

The first new lesson draft should be a source-data draft first.

Recommended candidate:

```text
Canada Life & Career English U1-L3 — Phone Plans & Internet
```

Alternative candidate:

```text
Travel English U1-L2 — Airport Check-in / Transportation Travel Lesson
```

## Why Canada Life L03 First

| Reason | Explanation |
|---|---|
| Main course | Canada Life & Career is the primary paid-course path |
| Stronger product fit | Phone / internet / setup topics are useful for newcomers and WHV students |
| v3.7 correction context exists | L03 was already part of the v3.7 correction discussion |
| Good conversion test | It can prove the JSON → template → HTML workflow before more expansion |

## Required Draft Format

First draft should be:

```text
lesson-data/ca-life/u1-l3.json
```

Not:

```text
lessons/ca-life/u1-l3.html
```

HTML should be generated only after source-data validation exists.

## Draft Requirements

For Canada Life A2:

```text
CATS = 5
Core = 25
Extended = 30
Phrases = 5
Dialogues = 5
Speaking = 5
Culture = 2
Pronunciation = 1 spotlight
```

## Draft Safety Rules

Before generating L03 source data:

```text
[ ] L02 JSON proof or extraction path is stable.
[ ] Course production rules are loaded.
[ ] Lesson registry row exists.
[ ] Previously Learned source is available from L01 and L02.
[ ] No HTML is generated directly.
[ ] Senior ESL Reviewer gate is applied.
```

## Current Status

```text
First New Lesson Draft Plan complete.
Actual L03 content draft not started.
```
