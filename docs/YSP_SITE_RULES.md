# YSP Site Rules

## Project Identity

Brand:

```text
YSP Learn & Shine
```

Slogan:

```text
Learn with Purpose. Shine with Confidence.
```

Repository:

```text
jobimtg/AT-vocab
```

Website:

```text
https://jobimtg.github.io/AT-vocab/
```

This is a GitHub Pages static site.

All public paths must work as relative paths. No server-side logic is available.

---

## Folder Structure

Root folders:

```text
assets/
docs/
js/
lessons/
scripts/
.github/workflows/
```

Course folders:

```text
lessons/ca-life/
lessons/travel/
lessons/business/
```

Assets subfolders inside each course:

```text
lessons/ca-life/assets/pronunciation/
lessons/ca-life/assets/phrases/
lessons/ca-life/assets/dialogues/
lessons/ca-life/assets/speaking/
lessons/ca-life/assets/culture/

lessons/travel/assets/pronunciation/
lessons/travel/assets/phrases/
lessons/travel/assets/dialogues/
lessons/travel/assets/speaking/
lessons/travel/assets/culture/

lessons/business/assets/pronunciation/
lessons/business/assets/phrases/
lessons/business/assets/dialogues/
lessons/business/assets/speaking/
lessons/business/assets/culture/
```

Do not create per-lesson asset folders such as:

```text
lessons/ca-life/u1-l1/assets/
lessons/travel/u1-l2/assets/
```

Images should live in the course-level shared `assets/` folder.

---

## Lesson File Naming

Lesson HTML files follow this pattern:

```text
u1-l1.html
u1-l2.html
u2-l1.html
```

Examples:

```text
lessons/ca-life/u1-l1.html
lessons/travel/u1-l1.html
lessons/business/u1-l1.html
```

---

## Lesson Image Prefix Rule

Image filenames use a lesson sequence prefix:

```text
l01
l02
l03
```

The prefix is a manually assigned lesson sequence number that matches the lesson's approved metadata and existing file naming plan.

It is not automatically calculated from the unit and lesson numbers in the HTML filename.

For example:

```text
u1-l1.html may use l01
u1-l2.html may use l02
u2-l1.html may use l03 or another approved prefix
```

When in doubt, check the existing image files in the course assets folder and the approved lesson plan.

---

## Future Lesson Registry

Because lesson image prefixes are manually assigned, a future registry file should be created later.

Possible locations:

```text
docs/YSP_LESSON_REGISTRY.md
```

or:

```text
lesson-data/lesson_registry.json
```

The registry should eventually track:

```text
course
lesson HTML path
lesson title
assigned image prefix
publish status
```

Example:

```text
ca-life | lessons/ca-life/u1-l1.html | Welcome to Canada | l01 | published
ca-life | lessons/ca-life/u1-l2.html | Getting a Phone Plan | l02 | draft
travel  | lessons/travel/u1-l1.html  | At the Airport | l01 | published
```

Until the registry exists, use the approved lesson plan and existing image filenames as the source of truth.

---

## Image Naming Rules

Image filename examples for a lesson assigned prefix `l01`:

```text
assets/pronunciation/l01-pronunciation-1.png
assets/pronunciation/l01-pronunciation-2.png

assets/phrases/l01-phrases-1.png
assets/phrases/l01-phrases-2.png

assets/dialogues/l01-d01-model.png
assets/dialogues/l01-d01-practice.png
assets/dialogues/l01-d01-extra-1.png
assets/dialogues/l01-d01-extra-2.png

assets/speaking/l01-speaking-1.png
assets/speaking/l01-speaking-2.png

assets/culture/l01-culture-1.png
assets/culture/l01-culture-2.png
assets/culture/l01-culture-3.png
assets/culture/l01-culture-4.png
```

Supported image formats:

```text
.png
.jpg
.jpeg
.webp
```

---

## Image Prefix Matching Rule

Gallery prefixes must include a trailing hyphen.

Correct prefixes:

```text
l01-pronunciation-
l01-phrases-
l01-speaking-
l01-culture-
```

Dialogue prefixes are per topic:

```text
l01-d01-
l01-d02-
l01-d03-
```

The trailing hyphen reduces accidental matches such as:

```text
l01-pronunciationGuide.png
l01-pronunciation2.png
```

However, the trailing hyphen does not prevent every invalid filename. For example, this still starts with `l01-pronunciation-`:

```text
l01-pronunciation-extra-notes.png
```

Therefore, automation should also follow stricter allowed suffix patterns.

---

## Allowed Image Suffix Patterns

### Pronunciation

Allowed:

```text
l01-pronunciation-1.png
l01-pronunciation-2.png
l01-pronunciation-3.png
```

Pattern:

```text
l01-pronunciation-[number].[extension]
```

---

### Useful Phrases

Allowed:

```text
l01-phrases-1.png
l01-phrases-2.png
l01-phrases-3.png
```

Pattern:

```text
l01-phrases-[number].[extension]
```

---

### Speaking Questions

Allowed:

```text
l01-speaking-1.png
l01-speaking-2.png
l01-speaking-3.png
```

Pattern:

```text
l01-speaking-[number].[extension]
```

---

### Culture

Allowed:

```text
l01-culture-1.png
l01-culture-2.png
l01-culture-3.png
l01-culture-4.png
```

Pattern:

```text
l01-culture-[number].[extension]
```

---

### Dialogue Practice

Allowed:

```text
l01-d01-model.png
l01-d01-practice.png
l01-d01-extra-1.png
l01-d01-extra-2.png
l01-d02-model.png
l01-d02-practice.png
l01-d02-extra-1.png
```

Patterns:

```text
l01-d01-model.[extension]
l01-d01-practice.[extension]
l01-d01-extra-[number].[extension]
```

Replace `d01` with the correct dialogue topic number.

---

## Dialogue Image Ordering Rule

Dialogue galleries should render images in this teaching order:

```text
1. model
2. practice
3. extra-1
4. extra-2
5. extra-3
```

Example:

```text
l01-d01-model.png
l01-d01-practice.png
l01-d01-extra-1.png
l01-d01-extra-2.png
```

Do not rely on plain alphabetical sorting for dialogue images if it causes model / practice / extra images to appear in the wrong order.

---

## Relative Path Rule

All `src` and `href` attributes inside lesson HTML must use relative paths.

From a lesson at:

```text
lessons/ca-life/u1-l1.html
```

Correct:

```text
assets/pronunciation/l01-pronunciation-1.png
../../js/ysp-global-nav.js
../../lessons/
```

Wrong:

```text
/assets/pronunciation/l01-pronunciation-1.png
https://jobimtg.github.io/AT-vocab/assets/...
lessons/ca-life/assets/pronunciation/l01-pronunciation-1.png
```

Absolute paths can break on GitHub Pages subpaths.

---

## Dynamic Image Gallery v3 — Canonical Structure

The Dynamic Image Gallery v3 system uses an outer persistent gallery container and an inner mount area.

The workflow must preserve the outer container and all data attributes.

The workflow may only replace the content inside the inner mount markers.

Canonical structure:

```html
<!-- YSP_IMAGE_GALLERY_START: l01-culture -->
<section
  class="ysp-image-gallery"
  data-ysp-gallery="l01-culture"
  data-ysp-image-dir="assets/culture"
  data-ysp-image-prefix="l01-culture-"
  data-ysp-image-title="Culture — 圖片版"
  data-ysp-image-subtitle="Culture gallery">

  <div class="ysp-image-gallery-head green">
    <span>Culture — 圖片版</span>
    <small>Culture gallery</small>
  </div>

  <div class="ysp-image-gallery-mount">
    <!-- YSP_IMAGE_GALLERY_MOUNT_START -->
    <div class="ysp-image-placeholder">
      圖片尚未更新
      <code>assets/culture/l01-culture-*.png</code>
    </div>
    <!-- YSP_IMAGE_GALLERY_MOUNT_END -->
  </div>
</section>
<!-- YSP_IMAGE_GALLERY_END: l01-culture -->
```

---

## Gallery Attributes

| Attribute                   | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| `class="ysp-image-gallery"` | Marks the section as a gallery container |
| `data-ysp-gallery`          | Unique gallery ID within the lesson page |
| `data-ysp-image-dir`        | Relative image folder path               |
| `data-ysp-image-prefix`     | Filename prefix used to match images     |
| `data-ysp-image-title`      | Display title for the gallery            |
| `data-ysp-image-subtitle`   | Display subtitle for the gallery         |

Use `data-ysp-image-dir` without a trailing slash.

Correct:

```html
data-ysp-image-dir="assets/culture"
```

Avoid:

```html
data-ysp-image-dir="assets/culture/"
```

---

## Inner Mount Point Rule

The workflow may replace only the content between:

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START -->
...
<!-- YSP_IMAGE_GALLERY_MOUNT_END -->
```

The workflow must not remove:

```text
the outer <section class="ysp-image-gallery">
data-ysp-gallery
data-ysp-image-dir
data-ysp-image-prefix
data-ysp-image-title
data-ysp-image-subtitle
the .ysp-image-gallery-mount wrapper
the YSP_IMAGE_GALLERY_MOUNT_START marker
the YSP_IMAGE_GALLERY_MOUNT_END marker
```

This rule is required for idempotency.

If the workflow removes the element containing `data-ysp-image-dir` and `data-ysp-image-prefix`, the first workflow run may appear successful, but the second run will no longer know where to find the images.

---

## Workflow Image Rendering Example

When matching images exist, the inner mount content may become:

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START -->
<div class="ysp-image-gallery-grid">
  <img src="assets/culture/l01-culture-1.png" alt="l01-culture-1" loading="lazy">
  <img src="assets/culture/l01-culture-2.png" alt="l01-culture-2" loading="lazy">
  <img src="assets/culture/l01-culture-3.png" alt="l01-culture-3" loading="lazy">
</div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END -->
```

When no matching images exist, the inner mount content should remain a placeholder:

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START -->
<div class="ysp-image-placeholder">
  圖片尚未更新
  <code>assets/culture/l01-culture-*.png</code>
</div>
<!-- YSP_IMAGE_GALLERY_MOUNT_END -->
```

The workflow must not create broken `<img>` tags.

---

## Required Gallery Blocks Per Lesson

Every lesson HTML that includes the corresponding image-based section should include the matching gallery block.

If a course template explicitly requires all five sections, then all five gallery blocks should exist.

If a lesson does not include a specific section, do not create a fake section only for the gallery.

Original text content for each section must remain in the page alongside the gallery.

The gallery is an addition, not a replacement.

---

## Useful Phrases Gallery

```html
<!-- YSP_IMAGE_GALLERY_START: l01-phrases -->
<section
  class="ysp-image-gallery"
  data-ysp-gallery="l01-phrases"
  data-ysp-image-dir="assets/phrases"
  data-ysp-image-prefix="l01-phrases-"
  data-ysp-image-title="Useful Phrases — 圖片版"
  data-ysp-image-subtitle="句型總覽圖片">

  <div class="ysp-image-gallery-head accent">
    <span>Useful Phrases — 圖片版</span>
    <small>句型總覽圖片</small>
  </div>

  <div class="ysp-image-gallery-mount">
    <!-- YSP_IMAGE_GALLERY_MOUNT_START -->
    <div class="ysp-image-placeholder">
      圖片尚未更新
      <code>assets/phrases/l01-phrases-*.png</code>
    </div>
    <!-- YSP_IMAGE_GALLERY_MOUNT_END -->
  </div>
</section>
<!-- YSP_IMAGE_GALLERY_END: l01-phrases -->
```

---

## Pronunciation Spotlight Gallery

```html
<!-- YSP_IMAGE_GALLERY_START: l01-pronunciation -->
<section
  class="ysp-image-gallery"
  data-ysp-gallery="l01-pronunciation"
  data-ysp-image-dir="assets/pronunciation"
  data-ysp-image-prefix="l01-pronunciation-"
  data-ysp-image-title="Pronunciation Spotlight — 圖片版"
  data-ysp-image-subtitle="發音焦點圖片">

  <div class="ysp-image-gallery-head alert">
    <span>Pronunciation Spotlight — 圖片版</span>
    <small>發音焦點圖片</small>
  </div>

  <div class="ysp-image-gallery-mount">
    <!-- YSP_IMAGE_GALLERY_MOUNT_START -->
    <div class="ysp-image-placeholder">
      圖片尚未更新
      <code>assets/pronunciation/l01-pronunciation-*.png</code>
    </div>
    <!-- YSP_IMAGE_GALLERY_MOUNT_END -->
  </div>
</section>
<!-- YSP_IMAGE_GALLERY_END: l01-pronunciation -->
```

---

## Dialogue Practice Gallery

Each dialogue topic must have its own gallery.

Do not use one broad prefix such as:

```text
l01-d
```

Use per-topic prefixes:

```text
l01-d01-
l01-d02-
l01-d03-
```

Dialogue 1 example:

```html
<!-- YSP_IMAGE_GALLERY_START: l01-d01 -->
<section
  class="ysp-image-gallery"
  data-ysp-gallery="l01-d01"
  data-ysp-image-dir="assets/dialogues"
  data-ysp-image-prefix="l01-d01-"
  data-ysp-image-title="Dialogue 1 — 圖片版"
  data-ysp-image-subtitle="Model / Practice / Extra images">

  <div class="ysp-image-gallery-head">
    <span>Dialogue 1 — 圖片版</span>
    <small>Model / Practice / Extra images</small>
  </div>

  <div class="ysp-image-gallery-mount">
    <!-- YSP_IMAGE_GALLERY_MOUNT_START -->
    <div class="ysp-image-placeholder">
      圖片尚未更新
      <code>assets/dialogues/l01-d01-*.png</code>
    </div>
    <!-- YSP_IMAGE_GALLERY_MOUNT_END -->
  </div>
</section>
<!-- YSP_IMAGE_GALLERY_END: l01-d01 -->
```

Dialogue 2 example:

```html
<!-- YSP_IMAGE_GALLERY_START: l01-d02 -->
<section
  class="ysp-image-gallery"
  data-ysp-gallery="l01-d02"
  data-ysp-image-dir="assets/dialogues"
  data-ysp-image-prefix="l01-d02-"
  data-ysp-image-title="Dialogue 2 — 圖片版"
  data-ysp-image-subtitle="Model / Practice / Extra images">

  <div class="ysp-image-gallery-head">
    <span>Dialogue 2 — 圖片版</span>
    <small>Model / Practice / Extra images</small>
  </div>

  <div class="ysp-image-gallery-mount">
    <!-- YSP_IMAGE_GALLERY_MOUNT_START -->
    <div class="ysp-image-placeholder">
      圖片尚未更新
      <code>assets/dialogues/l01-d02-*.png</code>
    </div>
    <!-- YSP_IMAGE_GALLERY_MOUNT_END -->
  </div>
</section>
<!-- YSP_IMAGE_GALLERY_END: l01-d02 -->
```

---

## Speaking Questions Gallery

```html
<!-- YSP_IMAGE_GALLERY_START: l01-speaking -->
<section
  class="ysp-image-gallery"
  data-ysp-gallery="l01-speaking"
  data-ysp-image-dir="assets/speaking"
  data-ysp-image-prefix="l01-speaking-"
  data-ysp-image-title="Speaking Questions — 圖片版"
  data-ysp-image-subtitle="口說題目圖片">

  <div class="ysp-image-gallery-head teal">
    <span>Speaking Questions — 圖片版</span>
    <small>口說題目圖片</small>
  </div>

  <div class="ysp-image-gallery-mount">
    <!-- YSP_IMAGE_GALLERY_MOUNT_START -->
    <div class="ysp-image-placeholder">
      圖片尚未更新
      <code>assets/speaking/l01-speaking-*.png</code>
    </div>
    <!-- YSP_IMAGE_GALLERY_MOUNT_END -->
  </div>
</section>
<!-- YSP_IMAGE_GALLERY_END: l01-speaking -->
```

---

## Culture Gallery

```html
<!-- YSP_IMAGE_GALLERY_START: l01-culture -->
<section
  class="ysp-image-gallery"
  data-ysp-gallery="l01-culture"
  data-ysp-image-dir="assets/culture"
  data-ysp-image-prefix="l01-culture-"
  data-ysp-image-title="Culture — 圖片版"
  data-ysp-image-subtitle="Culture gallery">

  <div class="ysp-image-gallery-head green">
    <span>Culture — 圖片版</span>
    <small>Culture gallery</small>
  </div>

  <div class="ysp-image-gallery-mount">
    <!-- YSP_IMAGE_GALLERY_MOUNT_START -->
    <div class="ysp-image-placeholder">
      圖片尚未更新
      <code>assets/culture/l01-culture-*.png</code>
    </div>
    <!-- YSP_IMAGE_GALLERY_MOUNT_END -->
  </div>
</section>
<!-- YSP_IMAGE_GALLERY_END: l01-culture -->
```

---

## Original Text Content Rule

Original lesson text content must always be preserved in full.

This includes:

```text
vocabulary cards
drilling exercises
useful phrases
pronunciation text
dialogues
role-play prompts
speaking questions
culture notes
review tasks
JavaScript lesson data
```

Gallery blocks are additions.

They must appear alongside the original text content for their section, not in place of it.

Claude and workflow must never:

```text
delete text content sections
replace text content with image gallery blocks
remove vocabulary card arrays
remove JavaScript lesson data
rewrite full lesson HTML unnecessarily
```

---

## Gallery Updater Boundary

The gallery updater may only update image-rendered content inside:

```html
<!-- YSP_IMAGE_GALLERY_MOUNT_START -->
...
<!-- YSP_IMAGE_GALLERY_MOUNT_END -->
```

The gallery updater must not modify:

```text
lesson text content
gallery outer section
gallery data attributes
headings
navigation
lesson cards
homepage featured cards
workflow files
```

---

## Site Maintenance Boundary

The site maintenance script may update explicitly generated site infrastructure only.

Allowed site infrastructure updates include:

```text
adding or repairing one YSP_GLOBAL_NAV_LOADER block
removing legacy generated nav blocks from old patch workflows
removing duplicate generated Top buttons
removing duplicate generated Back to Lessons buttons
updating lessons/index.html lesson cards
updating index.html featured lesson cards
removing internal production notes
normalizing generated wrappers if explicitly documented
```

The site maintenance script must not rewrite original lesson teaching content.

If content must be changed, it requires a separate user-approved content update task.

---

## Prohibited Actions — Claude and Workflow

Claude and the workflow must never:

```text
delete text content from lesson pages
replace text content with images
hard-code nav, Top button, or Back to Lessons inline in HTML
use a broad dialogue prefix such as l01-d instead of per-topic prefixes such as l01-d01-
omit the trailing hyphen from image prefixes
hard-code a fixed image count
rewrite full lesson HTML unless the user explicitly requests it
commit when no files have actually changed
create report folders
restore old patch workflows
add duplicate YSP_GLOBAL_NAV_LOADER blocks
add duplicate Top buttons
add duplicate Back to Lessons buttons
remove gallery data attributes during image rendering
remove YSP_IMAGE_GALLERY_MOUNT markers during image rendering
```

---

## Navigation Rule

Every lesson HTML file must include exactly one global nav loader block placed before `</body>`:

```html
<!-- YSP_GLOBAL_NAV_LOADER_START -->
<script src="../../js/ysp-global-nav.js" defer data-ysp-base="../../"></script>
<!-- YSP_GLOBAL_NAV_LOADER_END -->
```

The relative prefix must match the lesson's depth in the folder tree.

All navigation rendering is handled exclusively by:

```text
js/ysp-global-nav.js
```

This includes:

```text
top nav bar
Back to Lessons button
Top button
```

Lesson HTML files must not hard-code any of these navigation elements.

---

## Gallery Image Discovery Rule

When the workflow scans for gallery images:

1. It finds each outer `.ysp-image-gallery` section.
2. It reads `data-ysp-image-dir`.
3. It reads `data-ysp-image-prefix`.
4. It resolves the folder relative to the lesson HTML file.
5. It searches for supported image files whose names match the allowed prefix and suffix pattern.
6. It supports `.png`, `.jpg`, `.jpeg`, and `.webp`.
7. It sorts standard numbered galleries using natural sort.
8. It sorts dialogue galleries by model, practice, extra-1, extra-2, extra-3.
9. It does not assume a fixed image count.
10. If no matching images exist, it keeps or renders a placeholder.
11. It never creates broken `<img>` tags.
12. It preserves the gallery data attributes and mount markers.

---

## Active Workflows

Only these workflows should remain active:

```text
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

Do not restore old patch workflows.

If the repository still contains older workflow files, they must be reviewed separately before deletion or migration.

---

## Future Workflow Responsibilities

The site maintenance workflow is responsible for:

```text
scanning lesson HTML for YSP_IMAGE_GALLERY_START / END sections
reading data-ysp-image-dir and data-ysp-image-prefix
finding matching image files using the approved matching rules
rendering img tags for found images
preserving placeholder when no images exist
supporting png, jpg, jpeg, webp
updating lessons/index.html lesson cards
updating index.html featured lesson cards
adding YSP_GLOBAL_NAV_LOADER to lesson pages that are missing it
removing legacy generated nav blocks from old patch workflows
removing internal production notes
committing only when files actually changed
```

The progress dashboard workflow is display-only.

It must not modify files or commit.

---

## Idempotency Rule

The maintenance process must be safe to run repeatedly.

Running it twice must not create:

```text
duplicate headers
duplicate Back to Lessons buttons
duplicate Top buttons
duplicate gallery blocks
duplicate lesson cards
extra commits when nothing changed
```

Running maintenance twice should produce no diff on the second run.

---

## Validation Checklist Before Publishing a Lesson

```text
[ ] Lesson file is named correctly, for example u1-l1.html
[ ] Lesson is in the correct course folder
[ ] Lesson HTML contains exactly one YSP_GLOBAL_NAV_LOADER block
[ ] No inline nav, Top button, or Back to Lessons is hard-coded in HTML
[ ] No duplicate generated blocks exist
[ ] Original text content is intact
[ ] HTML still contains original section text above or near each gallery
[ ] Each image-based section has an outer YSP_IMAGE_GALLERY_START / END block when that section exists
[ ] Each image-based section has an inner YSP_IMAGE_GALLERY_MOUNT_START / END block
[ ] Every gallery id is unique within the lesson page
[ ] Gallery data attributes remain after maintenance workflow runs
[ ] YSP_IMAGE_GALLERY_MOUNT markers remain after image rendering
[ ] Gallery mount prevents horizontal overflow and the gallery grid uses a single `minmax(0, 1fr)` column
[ ] Rendered Gallery images use `width: 100%`, `max-width: 100%`, `height: auto`, `aspect-ratio: 16/9`, and `object-fit: contain`
[ ] A 1920×1080 source image stays inside the lesson content panel at desktop and mobile widths
[ ] data-ysp-image-dir uses a relative path such as assets/culture
[ ] data-ysp-image-dir does not use a trailing slash
[ ] data-ysp-image-prefix includes the correct l01 / l02 / l03 prefix and trailing hyphen
[ ] Each dialogue topic has its own per-topic dialogue gallery, such as l01-d01-, l01-d02-
[ ] Dialogue images appear in model → practice → extra order
[ ] No non-gallery images are accidentally matched by prefix
[ ] Image files are in the correct course assets subfolder
[ ] Image files use supported formats: png, jpg, jpeg, webp
[ ] No broken image tags point to nonexistent files
[ ] No internal production notes are visible in rendered HTML
[ ] lessons/index.html lesson card is correct
[ ] index.html featured lesson section is correct if the lesson is featured
[ ] Maintenance workflow runs twice without creating a new commit on the second run
```

---

## Black Swan Checks

Before modifying automation, always check for these risks:

```text
A workflow that removes gallery data attributes after the first run
A workflow that removes YSP_IMAGE_GALLERY_MOUNT markers after rendering images
A workflow that commits repeatedly with no real changes
A workflow that rewrites lesson teaching content
A workflow that restores old duplicate nav or Top button blocks
A workflow that matches unintended images because prefix rules are too broad
A workflow that breaks GitHub Pages relative paths
A workflow that hard-codes image counts instead of discovering available files
A workflow that uses stale workflow names from old project phases
```

If any of these risks are found, stop and fix the rule or script before publishing new lessons.

---

## Implementation Order

Do not create more course pages yet.

First stabilize:

```text
docs/YSP_SITE_RULES.md
scripts/ysp_validate_site.py
scripts/ysp_site_maintenance.py
js/ysp-global-nav.js
.github/workflows/ysp-site-maintenance.yml
.github/workflows/ysp-progress-dashboard.yml
```

After that:

```text
Create or finalize lesson JSON schema
Create lesson registry
Convert first lesson into true Free Preview format
Build first Full Practice Pack
Test with existing students
Add purchase/contact/waitlist pathway
```
