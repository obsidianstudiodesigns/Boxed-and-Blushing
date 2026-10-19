"""Key the green-screen cut-outs for the hero unboxing scene into transparent WebP layers.

Sources: research/gen/unbox-*.png (generated on a flat #00FF00 background)
Run from the project root:  python tools/make-unbox.py
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "research" / "gen"
OUT = ROOT / "assets" / "img" / "unbox"
OUT.mkdir(parents=True, exist_ok=True)

# name: (output width, soft key range). Glass needs a softer key so it stays see-through.
LAYERS = {
    "base": (900, (18, 70)),
    "lid": (900, (18, 70)),
    "robe": (480, (18, 70)),
    "flute": (220, (10, 120)),
    "slippers": (560, (18, 70)),
    "peonies": (620, (18, 70)),
}


def key(img, lo, hi):
    a = np.asarray(img.convert("RGB")).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    spill = g - np.maximum(r, b)          # how much greener than it should be
    alpha = 1.0 - np.clip((spill - lo) / (hi - lo), 0, 1)
    # Despill: pull green back down to the other channels where it leaks.
    g2 = np.minimum(g, np.maximum(r, b) + 4)
    out = np.dstack([r, g2, b, alpha * 255]).clip(0, 255).astype(np.uint8)
    im = Image.fromarray(out, "RGBA")
    # Tidy the edge: shrink the matte by a hair and soften it.
    al = im.getchannel("A").filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    im.putalpha(al)
    return im


for name, (width, (lo, hi)) in LAYERS.items():
    im = key(Image.open(GEN / f"unbox-{name}.png"), lo, hi)
    bbox = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    im = im.crop(bbox)
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(OUT / f"{name}.webp", "WEBP", quality=86, method=6)
    im.save(ROOT / "research" / f"unbox-{name}.png")
    print(f"{name}: {im.width}x{im.height}")

# Front wall of the box, from the front gold rim down. It sits above the rising gifts so they come out from inside.
base = Image.open(OUT / "base.webp")
RIM = round(base.height * 400 / 743)
base.crop((0, RIM, base.width, base.height)).save(OUT / "base-front.webp", "WEBP", quality=86, method=6)
print(f"base-front from y={RIM} of {base.height}")
