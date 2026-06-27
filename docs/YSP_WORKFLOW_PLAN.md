# YSP Workflow Plan

## Current Workflow Strategy

The project should use only two workflows.

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

This replaces the earlier patch-workflow system.

## Workflow 1 — YSP Site Maintenance

Path:

```text
.github/workflows/ysp-site-maintenance.yml
```

Purpose:

```text
Maintain lesson pages
Update lesson cards
Update homepage featured lessons
Attach global nav loader
Remove legacy generated blocks
Remove internal notes
Handle pronunciation image display
```

Recommended final structure:

```yaml
name: YSP Site Maintenance

on:
  workflow_dispatch:
  push:
    branches:
      - main
    paths:
      - "lessons/**/*.html"
      - "index.html"
      - "lessons/index.html"
      - "js/ysp-global-nav.js"
      - "scripts/ysp_site_maintenance.py"
      - ".github/workflows/ysp-site-maintenance.yml"

permissions:
  contents: write

jobs:
  ysp-site-maintenance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python3 scripts/ysp_site_maintenance.py
      - run: commit changes if needed
```

The workflow should not contain a huge embedded Python script.

## Workflow 2 — YSP Progress Dashboard

Path:

```text
.github/workflows/ysp-progress-dashboard.yml
```

Purpose:

```text
Display current progress in GitHub Actions Summary
Do not modify files
Do not commit
Do not create report folders
```

Dashboard should check current architecture:

```text
index.html exists
lessons/index.html exists
js/ysp-global-nav.js exists
scripts/ysp_site_maintenance.py exists
scripts/ysp_validate_site.py exists
.github/workflows/ysp-site-maintenance.yml exists
.github/workflows/ysp-progress-dashboard.yml exists
old workflows are removed
no report folder exists
at least one lesson exists
at least one lesson has global nav loader
```

## Old Workflows Not To Restore

Do not restore:

```text
auto-update-lessons-after-upload.yml
refresh-lesson-navigation.yml
check-course-links-v3-report-only.yml
check-course-links-v2.yml
check-site-links.yml
add-lesson-navigation.yml
add-lesson-navigation-v2.yml
auto-update-lessons-clean-header.yml
clean-homepage-layout.yml
clean-lessons-layout.yml
fix-top-button-overlap.yml
fix-practice-pack-placement.yml
fix-revenue-sections-placement.yml
fix-step1-sections-placement-combined.yml
step1-revenue-positioning.yml
update-ysp-progress-tracker.yml
```

## Next Workflow Task

The next workflow-related task is:

```text
Refactor ysp-site-maintenance.yml so it calls scripts/ysp_site_maintenance.py instead of embedding Python directly in YAML.
```
