# YSP Project Status

## Current Project

YSP Learn & Shine is a GitHub Pages English-learning website.

Website:

```text
https://jobimtg.github.io/AT-vocab/
```

Repository:

```text
jobimtg/AT-vocab
```

## Completed

### Brand

| Item | Status |
|---|---|
| Brand name: YSP Learn & Shine | Done |
| Slogan: Learn with Purpose. Shine with Confidence. | Done |
| Footer brand year: EST. 2026 | Done |
| Public positioning: Preview + Practice Pack + Trial Lesson | Done |

### Website Pages

| Page / Area | Status |
|---|---|
| Homepage clean layout | Done |
| Homepage CTA structure | Done |
| Lessons page clean layout | Done |
| Course folders | Done |
| Lesson page global navigation direction | Done / needs validation |
| Top button duplicate issue | Debugged conceptually / must be validated |
| Pronunciation image display | Needs fix / validation |

### Workflows

Current active workflows:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

Workflow cleanup status:

| Item | Status |
|---|---|
| Many patch workflows removed | Done |
| Maintenance workflow centralized | In progress |
| Progress dashboard display-only | Done / needs update |
| Python still embedded in YAML | Not done |
| Dedicated maintenance script | Not done |
| Validation script | Not done |

## Not Completed Yet

### Engineering

| Item | Priority | Status |
|---|---:|---|
| Move embedded Python into `scripts/ysp_site_maintenance.py` | High | Not done |
| Verify or create `js/ysp-global-nav.js` | High | Not done / unknown |
| Update `ysp-progress-dashboard.yml` for current two-workflow system | High | Not done |
| Add `docs/YSP_SITE_RULES.md` | High | Prepared in this handoff |
| Add `scripts/ysp_validate_site.py` | High | Not done |
| Make maintenance workflow idempotent | High | Needs validation |
| Add pronunciation image auto-display logic | High | Needs fix |

### Content Product

| Item | Priority | Status |
|---|---:|---|
| First Free Preview Lesson model | High | Not done |
| First Full Practice Pack | High | Not done |
| Practice Pack PDF template | Medium | Not done |
| Test with existing students | Medium | Not done |
| Payment / purchase path | Low | Not done |

### Marketing / Conversion

| Item | Priority | Status |
|---|---:|---|
| Beacons integration | Medium | Not done |
| Contact or waitlist form | Medium | Not done |
| SEO / Open Graph metadata | Medium | Not done |
| Payhip / Ko-fi / Gumroad decision | Low | Not done |

## Recommended Current Focus

Do not create more course pages yet.

Stabilize the engineering system first:

```text
scripts/ysp_site_maintenance.py
js/ysp-global-nav.js
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
scripts/ysp_validate_site.py
```

Then move to content production:

```text
L01 Free Preview Lesson
L01 Full Practice Pack
Student testing
Purchase or contact pathway
```
