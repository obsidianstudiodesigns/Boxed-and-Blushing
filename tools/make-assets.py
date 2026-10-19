"""Build the web images, logo badge and favicon set for the Boxed and Blushing site.

Sources:
  research/fb/   photos downloaded from the Boxed and Blushing Facebook page (bb-01.jpg ... bb-70.jpg)
  research/gen/  photoreal images generated for the site (Figma AI)
  logo.jpg       the client's round logo

Run from the project root:  python tools/make-assets.py
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
FB = ROOT / "research" / "fb"
GEN = ROOT / "research" / "gen"
OUT = ROOT / "assets" / "img"
(OUT / "gallery").mkdir(parents=True, exist_ok=True)

BLUSH = (251, 240, 242)


def save_webp(img, path, quality=80):
    img.convert("RGB").save(path, "WEBP", quality=quality, method=6)


def fit_width(img, width):
    if img.width <= width:
        return img
    return img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)


def crop_ratio(img, ratio, focus_y=0.5, focus_x=0.5):
    """Crop to width/height = ratio around a focus point."""
    w, h = img.size
    if w / h > ratio:
        nw = round(h * ratio)
        left = round((w - nw) * focus_x)
        return img.crop((left, 0, left + nw, h))
    nh = round(w / ratio)
    top = round((h - nh) * focus_y)
    return img.crop((0, top, w, top + nh))


def fb(n):
    return Image.open(FB / f"bb-{n:02d}.jpg").convert("RGB")


# Box cards: (photo, output name, focus_y). Exported at their own ratio; CSS crops them to fit each card.
BOXES = [
    (20, "box-bridesmaid", 0.5),
    (42, "box-groomsmen", 0.5),
    (21, "box-bride", 0.5),
    (29, "box-mothers", 0.5),
    (61, "box-flowergirl", 0.45),
    (60, "box-ringsecurity", 0.5),
    (4, "box-21st", 0.5),
    (35, "box-matric", 0.5),
    (69, "box-baby", 0.5),
]
for n, name, fy in BOXES:
    img = fb(n)
    if img.height > img.width:
        img = crop_ratio(img, 4 / 5, fy)
    out = fit_width(img, 1100)
    save_webp(out, OUT / f"{name}.webp", quality=78)
    print(f"{name}: {out.width}x{out.height}")

# Add-on tiles, square.
EXTRAS = [(11, "extra-tumbler", 0.45), (18, "extra-candle", 0.5), (32, "extra-slippers", 0.5), (23, "extra-robe", 0.35)]
for n, name, fy in EXTRAS:
    save_webp(fit_width(crop_ratio(fb(n), 1, fy), 520), OUT / f"{name}.webp", quality=78)

# Review photo: Marisca's bridal party in their robes.
save_webp(fit_width(crop_ratio(fb(40), 3 / 4, 0.4), 640), OUT / "review-wedding.webp", quality=78)

# Gallery: natural ratio, a thumbnail and a large view for the lightbox.
GALLERY = [23, 50, 57, 64, 38, 17, 13, 44, 26, 27, 10, 62, 46, 55, 33, 70, 52, 37]
for n in GALLERY:
    img = fb(n)
    save_webp(fit_width(img, 640), OUT / "gallery" / f"bb-{n:02d}-sm.webp", quality=74)
    save_webp(fit_width(img, 1400), OUT / "gallery" / f"bb-{n:02d}.webp", quality=80)
    sm = fit_width(img, 640)
    print(f"gallery bb-{n:02d}: {sm.width}x{sm.height}")

# Generated images.
hero = Image.open(GEN / "hero-box.png")
save_webp(hero, OUT / "hero-box.webp", quality=82)
save_webp(fit_width(hero, 600), OUT / "hero-box-sm.webp", quality=78)
build = Image.open(GEN / "build-flatlay.png")
save_webp(fit_width(build, 1400), OUT / "build-flatlay.webp", quality=80)
save_webp(fit_width(build, 800), OUT / "build-flatlay-sm.webp", quality=76)
stack = Image.open(GEN / "box-stack.png")
save_webp(fit_width(stack, 800), OUT / "box-stack.webp", quality=80)


# Logo: the round badge, transparent outside its outer ring.
logo = Image.open(ROOT / "logo.jpg").convert("RGBA")
LW, LH = logo.size


def badge(diameter, pad=0):
    """Full round logo, cut out of its white square."""
    cx, cy, r = LW // 2, LH // 2, min(LW, LH) // 2 - 4
    disc = logo.crop((cx - r, cy - r, cx + r, cy + r))
    size = r * 2
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    disc.putalpha(mask.resize((size, size), Image.LANCZOS))
    return disc.resize((diameter, diameter), Image.LANCZOS)


badge(240).save(OUT / "logo-badge.png", optimize=True)
badge(240).save(OUT / "logo-badge.webp", "WEBP", quality=90, method=6)


def monogram(size):
    """The pink gift box from the logo on a white disc with a blush ring. Reads better than the full logo when tiny."""
    mono = logo.crop((round(LW * 0.135), round(LH * 0.375), round(LW * 0.455), round(LH * 0.695)))
    scale = 4
    S = size * scale
    base = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(base)
    d.ellipse((0, 0, S - 1, S - 1), fill=(214, 128, 150, 255))
    ring = max(2, round(S * 0.045))
    d.ellipse((ring, ring, S - 1 - ring, S - 1 - ring), fill=(255, 253, 253, 255))
    inner = round(S * 0.86)
    m = mono.resize((inner, inner), Image.LANCZOS)
    base.alpha_composite(m, ((S - inner) // 2, (S - inner) // 2 + round(S * 0.01)))
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse((ring, ring, S - 1 - ring, S - 1 - ring), fill=255)
    # keep the ring itself
    outer = Image.new("L", (S, S), 0)
    ImageDraw.Draw(outer).ellipse((0, 0, S - 1, S - 1), fill=255)
    base.putalpha(outer)
    return base.resize((size, size), Image.LANCZOS)


monogram(32).save(ROOT / "favicon-32.png", optimize=True)
monogram(16).save(ROOT / "favicon-16.png", optimize=True)
monogram(48).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])


def on_blush(size, pad):
    base = Image.new("RGBA", (size, size), BLUSH + (255,))
    b = badge(size - 2 * pad)
    base.alpha_composite(b, (pad, pad))
    return base.convert("RGB")


on_blush(180, 8).save(ROOT / "apple-touch-icon.png", optimize=True)
on_blush(192, 8).save(ROOT / "icon-192.png", optimize=True)
on_blush(512, 60).save(ROOT / "icon-512.png", optimize=True)

print("assets written to", OUT)
