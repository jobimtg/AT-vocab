# YSP Image Inbox

Upload new lesson HTML and lesson image files into this folder when you want GitHub Actions to publish and sort them automatically.

The `YSP Site Maintenance` workflow watches `image-inbox/**`.

When a supported lesson HTML filename is uploaded here, the workflow publishes it into the correct course folder.

When a supported image filename is uploaded here, the workflow moves it into the correct course asset folder.

## Supported lesson HTML examples

```text
ca-life-u1-l3.html
travel-u1-l2.html
business-u2-l1.html
```

## Lesson HTML destination examples

```text
ca-life-u1-l3.html
→ lessons/ca-life/u1-l3.html

travel-u1-l2.html
→ lessons/travel/u1-l2.html

business-u2-l1.html
→ lessons/business/u2-l1.html
```

## Supported image examples

```text
ca-life-l02-pronunciation-1.png
ca-life-l02-phrases-1.png
ca-life-l02-speaking-1.png
ca-life-l02-culture-1.png
ca-life-l02-d01-model.png
ca-life-l02-d01-practice.png
ca-life-l02-d01-extra-1.png

travel-l01-pronunciation-1.png
business-l01-d01-model.png
```

## Image destination examples

```text
ca-life-l02-pronunciation-1.png
→ lessons/ca-life/assets/pronunciation/l02-pronunciation-1.png

ca-life-l02-d01-model.png
→ lessons/ca-life/assets/dialogues/l02-d01-model.png
```

## Safety rules

- Supported image file types: `.png`, `.jpg`, `.jpeg`, `.webp`
- Supported lesson HTML naming pattern: `<course>-u<number>-l<number>.html`
- Supported courses: `ca-life`, `travel`, `business`
- Existing lesson HTML files are not overwritten.
- Existing image files are not overwritten.
- If a target file already exists, the workflow skips the inbox file and reports the reason in the Actions log.
- Lesson HTML must already contain Dynamic Image Gallery blocks for images to appear automatically inside the lesson page.
- Core Vocabulary icons are inline SVG inside the HTML data array and should not be uploaded here.
