# YSP Lesson Data

This folder is the future source-data area for YSP Learn & Shine lessons.

## Core Rule

Lesson content should not be authored directly as HTML.

Recommended flow:

```text
lesson-data JSON / Markdown source
        ↓
fixed L02 renderer / template
        ↓
generated lesson HTML
        ↓
GitHub Pages
```

## Current Status

```text
Phase 2 Foundation: complete
Full source-data build pipeline: future implementation
```

## Folder Structure

```text
lesson-data/
  ca-life/
  travel/
  business/
```

## File Naming

Use the same unit / lesson pattern as public HTML output:

```text
u1-l1.json
u1-l2.json
u2-l1.json
```

## Required Source Data Sections

A full lesson source file should eventually include:

```text
meta
categories
core
extended
phrases
dialogues
speaking
culture
pronunciation
previously_learned
validation
```

## L02 Golden Source

The uploaded L02 file is the current Golden Template reference.

Full conversion should be done by local Codex or a repo script so the full data arrays can be extracted safely from:

```text
L02_transportation_fixed_teacher_notes.html
```

Do not manually retype large lesson arrays into GitHub by hand.
