# YSP ESL Skill Source Map

_Last updated: 2026-06-30_

## Purpose

This document explains how the uploaded ESL production and review files should be used in Phase 2.

These files are not casual references. They define the lesson production system.

## Uploaded Source Files

| Source File | Role | Use In Phase 2 |
|---|---|---|
| `esl-lesson-planner SKILL_v3.7_final.md` | Primary lesson-generation specification | Controls HTML lesson structure, counts, tab order, data schema, and validation |
| `senior-esl-reviewer.skill` | Pedagogical review skill | Reviews whether the lesson is teachable, realistic, speaking-focused, and suitable for online 1-on-1 ESL |
| `ESL_v3.7_FIX_REPORT_AND_VALIDATION.md` | Fix report and validation evidence | Explains why v3.7 exists and confirms corrected L03 validation expectations |
| `CLAUDE_ESL_v3.7_USAGE_GUIDE_PROJECT_INSTRUCTIONS.md` | Usage guide | Explains how to place short rules in Project Instructions and full skill in Project Knowledge / Skill folder |

## Correct Usage

Phase 2 must use these sources in this order:

```text
1. Use ESL Lesson Planner v3.7 to generate or structure lesson HTML.
2. Use Senior ESL Reviewer to review the teaching value and feasibility.
3. Use the v3.7 validation report to verify known failure points are avoided.
4. Use the usage guide to keep Claude / ChatGPT / Codex setup consistent.
```

## ESL Lesson Planner v3.7 Role

This is the hard technical production contract.

It controls:

```text
Golden L02 Template Lock
course profiles and required counts
10-tab order
data variables and schema
short class names
forbidden legacy patterns
Core card visual rules
mandatory validation checklist
Previously Learned rule
output rules
```

When generating lesson HTML, this file has priority over general style preferences.

## Senior ESL Reviewer Role

This is the teaching-quality gate.

It reviews:

```text
topic relevance
timing feasibility
cognitive load
vocabulary strategy
spiral review
speaking output
pronunciation
error correction
assessment
student autonomy
online 1-on-1 practicality
```

A lesson can be technically valid but still fail the Senior ESL review if it is impossible to teach in a real 25–50 minute online class.

## v3.7 Fix Report Role

This report explains why the v3.7 lock exists.

Known issues it prevents:

```text
new lessons using different card layouts
static .vocab-card HTML
wrong class names
wrong tab order
wrong Core / Extended counts
missing SVGs
missing practice blanks
broken familiarity filters
guessed Previously Learned data
```

Use it as a regression checklist when future generated lessons look different from the approved template.

## Usage Guide Role

This guide explains where to put the rules when using Claude.

Recommended setup:

```text
Project Instructions: short forced rules
Project Knowledge: full v3.7 skill and correct HTML examples
Claude Skills folder: full SKILL.md when using Claude Skills
```

The guide also explains that simply telling Claude to "refer to L02" is not enough. The short forced rules and full skill must be available.

## Repository Policy

The GitHub repo should not store `.skill` packages as the main source of truth unless explicitly approved.

For long-term maintainability, the repo should store normalized Markdown docs under:

```text
docs/
```

Current normalized repo documents:

```text
docs/YSP_PHASE2_CONTENT_PLAN.md
docs/YSP_GOLDEN_LESSON_TEMPLATE.md
docs/YSP_ESL_SKILL_SOURCE_MAP.md
docs/YSP_SITE_RULES.md
docs/YSP_PROJECT_STATUS.md
```

## Practical Rule

For any future lesson-production task, the workflow must be:

```text
Generate with v3.7 Golden L02 Template
Validate with v3.7 checklist
Review with Senior ESL Reviewer
Run site validator if HTML enters GitHub
Only then publish or merge
```
