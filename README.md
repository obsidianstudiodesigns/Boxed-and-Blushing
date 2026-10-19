# Boxed and Blushing

Landing page for Boxed and Blushing ("Thoughtful gifts, beautifully boxed. Made with love, just for you."), a South African business that makes personalised gift boxes: bridesmaid (strooimeisie) and groomsmen (strooijonker) boxes, bride and mother of the bride or groom gifts, flower girl and ring security boxes, 21st birthday, matric dance and new baby boxes, plus wedding extras. They deliver nationwide and take orders on WhatsApp (064 395 3029).

Live: https://obsidianstudiodesigns.github.io/Boxed-and-Blushing/

## What's on the site

- `index.html`: unboxing hero, occasions strip, box collection (10 boxes, each with "Add to order"), how it works, add-ons and wedding extras, gallery with photo viewer, reviews, order builder, FAQ, closing call-to-action
- **Unboxing hero.** The first screen is pinned while you scroll: the lid lifts off the gift box, light glows from inside and a satin bridal robe, champagne flute and slippers rise out, with peonies in front and petals drifting across the background (they move away from the mouse). Tapping the box opens it too. Built with GSAP ScrollTrigger (cdnjs) and a canvas for the petals. With reduced motion turned on, or if GSAP fails to load, the box simply shows open with no pinning.
- **WhatsApp ordering.** Visitors add boxes and extras to an order (kept in their own browser's local storage), change quantities, then fill in their name, the names to print, theme and colours, date needed, delivery town and notes. "Send my order on WhatsApp" opens WhatsApp to 064 395 3029 with the whole order written out. There is no backend.
- The bridal party special (buy 3 matching bridesmaid or groomsmen boxes, 4th free) shows on the page and in the order panel once 4 matching boxes are added.
- Light and dark mode follow the visitor's phone or computer setting.
- `privacy.html` (POPIA), `terms.html` (ECTA s43 disclosure, quotes, personalisation, delivery, specials, returns on personalised goods, safety), `404.html`
- SEO and sharing: canonical URLs, Open Graph and Twitter tags with `og-image.jpg` (1200 x 630) for WhatsApp previews, Store/LocalBusiness, WebSite and FAQPage JSON-LD, `sitemap.xml`, `robots.txt`, favicon set and web manifest

## Content sources

- Logo and banner from the client (`logo.jpg`, `banner.jpg`). The round logo is cut out for the header, footer and app icons. The gift box from the logo is the favicon.
- Box photos, gallery and the wedding photo: the client's own photos from the Facebook page.
- Generated photoreal images (Figma AI): the unboxing layers (box, lid, robe, flute, slippers, peonies, generated on green screen and keyed out), the bridesmaid box in the share image, the mix and match flat lay, and the stack of ribboned boxes.
- Facebook posts: box contents, the bridal party special, nationwide delivery, wedding extras (hangers, magnetic seating plan board, bottle opener key rings, infinity dresses).
- Reviews: Uane van der Schyff and Marisca Knott, from the Facebook page reviews.

## To confirm with Boxed and Blushing before promoting the site

- **Bridal party special.** Taken from a Facebook post. Confirm it is still running, or remove the banner in the boxes section and the note in the order panel.
- **Prices.** None are shown. The site says boxes are budget friendly and quoted on WhatsApp.
- **Location.** The Facebook page lists no town, so the site only says "delivered across South Africa". Add a town or area if they want local search traffic.
- Owner's name, legal status, address for legal notices, VAT number and payment methods for `terms.html` (marked `TO CONFIRM` in `tools/make-pages.py`).
- The 5-day window for reporting faulty or damaged items in `terms.html`.
- Whether they're happy for the named photos (first names on robes, boxes and tumblers) to be shown on the website.

## Tools

- `tools/make-assets.py`: builds the web images, logo badge and favicons from `research/` (local only, not committed) and `logo.jpg`
- `tools/make-unbox.py`: keys the green-screen unboxing layers into transparent WebP files in `assets/img/unbox/`
- `tools/make-pages.py`: writes the legal pages and 404 from one template
- `tools/og.html` + `tools/make-og.sh`: renders `og-image.jpg` with headless Chrome

## Local preview

```bash
python -m http.server 5194
```

## Deploying

GitHub Pages serves the `main` branch root. Commit and push to `main`.

Website designed by [Obsidian Studio Designs](https://obsidianstudiodesigns.co.za/).
