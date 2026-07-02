# YSP Phase 5 JSON Ready Note

_Last updated: 2026-07-02_

## Status

The full L02 JSON was generated locally from the confirmed Golden L02 HTML source.

The raw HTML source is not committed to the public repo.

## Local Generated File

```text
u1-l2.json
```

Expected repo destination:

```text
lesson-data/ca-life/u1-l2.json
```

## Local Validation Summary

```text
categories: 5 / 5
core: 25 / 25
extended: 30 / 30
phrases: 5 / 5
dialogues: 5 / 5
speaking: 5 / 5
culture: 2 / 2
pronunciation_words: 5 / 5
status: passed
```

## Why JSON Is Not In This PR

The current GitHub connector can create and update text files from message content, but it cannot safely attach a local generated file directly as a repo file.

The generated JSON is large enough that manually pasting it through chat would create unnecessary copy/paste risk.

Therefore this PR adds the validator, extraction report, and local Codex task first. The full JSON should be committed through a local/Codex-safe file operation.

## Next Safe Commit Scope

Only commit:

```text
lesson-data/ca-life/u1-l2.json
```

Do not commit:

```text
L02_transportation_fixed_teacher_notes.html
```
