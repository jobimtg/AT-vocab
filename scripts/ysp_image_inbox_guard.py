# Run with: python3 scripts/ysp_image_inbox_guard.py

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
IMAGE_INBOX = ROOT / "image-inbox"
OVERSIZE_DIR = IMAGE_INBOX / "_oversize"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

WARN_BYTES = 2 * 1024 * 1024
MAX_BYTES = 5 * 1024 * 1024


def human_size(num_bytes: int) -> str:
    return f"{num_bytes / (1024 * 1024):.2f} MB"


def main() -> None:
    print("YSP Image Inbox Guard")
    print("=====================")

    if not IMAGE_INBOX.exists():
        print("image-inbox/ does not exist. Nothing to check.")
        return

    checked = 0
    warned = []
    blocked = []

    for path in sorted(IMAGE_INBOX.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        checked += 1
        size = path.stat().st_size

        if size > MAX_BYTES:
            OVERSIZE_DIR.mkdir(parents=True, exist_ok=True)
            dest = OVERSIZE_DIR / path.name
            if dest.exists():
                stem = path.stem
                suffix = path.suffix
                index = 2
                while True:
                    candidate = OVERSIZE_DIR / f"{stem}-{index}{suffix}"
                    if not candidate.exists():
                        dest = candidate
                        break
                    index += 1
            shutil.move(str(path), str(dest))
            blocked.append((path.name, human_size(size), dest.relative_to(ROOT).as_posix()))
        elif size > WARN_BYTES:
            warned.append((path.name, human_size(size)))

    print(f"Images checked: {checked}")

    if warned:
        print(f"Images over warning level ({human_size(WARN_BYTES)}): {len(warned)}")
        for name, size in warned:
            print(f"- WARNING: {name} is {size}; target is under 1 MB when possible.")

    if blocked:
        print(f"Images blocked over max level ({human_size(MAX_BYTES)}): {len(blocked)}")
        for name, size, dest in blocked:
            print(f"- BLOCKED: {name} is {size}; moved to {dest}")

    if not warned and not blocked:
        print("All image-inbox images are within the configured size guard.")


if __name__ == "__main__":
    main()
