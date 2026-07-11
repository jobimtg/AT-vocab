# YSP Image Inbox

Upload new lesson image files into this folder when you want GitHub Actions to sort them automatically.

The `YSP Site Maintenance` workflow watches `image-inbox/**`. When a supported image filename is uploaded here, the workflow moves it into the correct course asset folder.

## Supported examples

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

## Destination examples

```text
ca-life-l02-pronunciation-1.png
→ lessons/ca-life/assets/pronunciation/l02-pronunciation-1.png

ca-life-l02-d01-model.png
→ lessons/ca-life/assets/dialogues/l02-d01-model.png
```

## Notes

- Supported file types: `.png`, `.jpg`, `.jpeg`, `.webp`
- Do not upload unrelated files here.
- If a target image already exists, the workflow will skip that file instead of overwriting it.
- Lesson HTML must already contain a Dynamic Image Gallery block for the image to appear automatically on the lesson page.
