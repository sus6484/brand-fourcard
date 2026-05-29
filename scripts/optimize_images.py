"""Generate web-optimized gallery thumbs/display and content images."""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "image"
GALLERY_DIR = IMAGE_DIR / "gallery"
THUMB_DIR = GALLERY_DIR / "thumbs"
DISPLAY_DIR = GALLERY_DIR / "display"
OPTIMIZED_DIR = IMAGE_DIR / "optimized"

THUMB_WIDTH = 480
DISPLAY_WIDTH = 1400
CONTENT_WIDTH = 1280


def save_webp(img: Image.Image, path: Path, quality: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rgb = img.convert("RGB") if img.mode not in ("RGB", "L") else img
    rgb.save(path, "WEBP", quality=quality, method=6)


def resize_to_width(img: Image.Image, width: int) -> Image.Image:
    if img.width <= width:
        return img
    ratio = width / img.width
    return img.resize((width, max(1, int(img.height * ratio))), Image.Resampling.LANCZOS)


def optimize_gallery() -> None:
    for path in sorted(GALLERY_DIR.glob("*.jpg")):
        img = Image.open(path)
        base = path.stem
        save_webp(resize_to_width(img, THUMB_WIDTH), THUMB_DIR / f"{base}.webp", 78)
        save_webp(resize_to_width(img, DISPLAY_WIDTH), DISPLAY_DIR / f"{base}.webp", 82)
        thumb_kb = (THUMB_DIR / f"{base}.webp").stat().st_size / 1024
        display_kb = (DISPLAY_DIR / f"{base}.webp").stat().st_size / 1024
        print(f"gallery {base}: thumb {thumb_kb:.0f}KB, display {display_kb:.0f}KB")


def optimize_content(name: str) -> None:
    path = IMAGE_DIR / name
    if not path.exists():
        return
    img = Image.open(path)
    stem = path.stem
    save_webp(resize_to_width(img, CONTENT_WIDTH), OPTIMIZED_DIR / f"{stem}.webp", 82)
    out_kb = (OPTIMIZED_DIR / f"{stem}.webp").stat().st_size / 1024
    print(f"content {name}: {out_kb:.0f}KB")


def main() -> None:
    optimize_gallery()
    for filename in ("02.jpg", "03.jpg"):
        optimize_content(filename)
    print("done")


if __name__ == "__main__":
    main()
