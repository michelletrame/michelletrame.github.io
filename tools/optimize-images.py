#!/usr/bin/env python3
"""Resize + convert source images to WebP for the site.

Usage: python3 tools/optimize-images.py SRC_DIR OUT_DIR
SRC_DIR holds one sub-folder per case study (e.g. apf/, vouch/).
Writes OUT_DIR/<slug>/<name>-800.webp and -1600.webp (never upscales),
and prints a manifest line per image: slug/name width height.
"""
import re, sys
from pathlib import Path
from PIL import Image, ImageOps

WIDTHS = (800, 1600)
src, out = Path(sys.argv[1]), Path(sys.argv[2])

def slugify(name):
    s = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    return s or 'image'

for folder in sorted(p for p in src.iterdir() if p.is_dir()):
    for f in sorted(folder.iterdir()):
        if f.suffix.lower() not in {'.jpg', '.jpeg', '.png', '.webp'}:
            continue
        im = ImageOps.exif_transpose(Image.open(f))
        im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
        name = slugify(f.stem)
        dest = out / folder.name
        dest.mkdir(parents=True, exist_ok=True)
        for w in WIDTHS:
            if w > im.width and w != WIDTHS[0]:
                continue
            r = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            r.save(dest / f'{name}-{w}.webp', 'WEBP', quality=80, method=6)
        print(f'{folder.name}/{name} {im.width} {im.height}')
