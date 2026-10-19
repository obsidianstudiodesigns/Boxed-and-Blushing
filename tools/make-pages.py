"""Write the legal pages and 404 page from one shared template.

Run from the project root:  python tools/make-pages.py
Edit the page bodies below, then re-run.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://obsidianstudiodesigns.github.io/Boxed-and-Blushing/"
UPDATED = "19 October 2026"
WA = "https://wa.me/27643953029"

HEAD = """<!doctype html>
<html lang="en-ZA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title} | Boxed and Blushing</title>
  <meta name="description" content="{desc}">
  {canonical}
  <meta name="theme-color" content="#fff8f8" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#1b1116" media="(prefers-color-scheme: dark)">
  <link rel="icon" href="favicon.ico" sizes="48x48">
  <link rel="icon" href="favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Boxed and Blushing">
  <meta property="og:locale" content="en_ZA">
  <meta property="og:title" content="{title} | Boxed and Blushing">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{base}og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/regular/style.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/fill/style.css">
  <link rel="stylesheet" href="assets/css/style.css?v=1">
</head>
<body>
  <header class="site-header legal-header">
    <div class="wrap header-inner">
      <a class="brand" href="./" aria-label="Boxed and Blushing, home page">
        <img src="assets/img/logo-badge.webp" alt="" width="50" height="50">
        <span class="brand-word">Boxed <em>&amp;</em> Blushing</span>
      </a>
      <a class="btn btn-primary btn-sm" href="{wa}" target="_blank" rel="noopener"><i class="ph-fill ph-whatsapp-logo" aria-hidden="true"></i>Chat on WhatsApp</a>
    </div>
  </header>
"""

FOOT = """
  <footer class="site-footer" style="padding-bottom:28px">
    <div class="wrap footer-base" style="margin-top:0;border-top:0;padding-top:0">
      <p>&copy; <span data-year>2026</span> Boxed and Blushing. All rights reserved.</p>
      <nav class="legal-nav" aria-label="Legal">
        <a href="privacy.html"{cur_privacy}>Privacy policy</a>
        <a href="terms.html"{cur_terms}>Terms of use</a>
      </nav>
      <p class="credit">Website designed by <a href="https://obsidianstudiodesigns.co.za/" target="_blank" rel="noopener">Obsidian Studio Designs</a></p>
    </div>
  </footer>
  <script>document.querySelectorAll('[data-year]').forEach(function (e) {{ e.textContent = new Date().getFullYear(); }});</script>
</body>
</html>
"""

CONTACT = """<dl>
      <dt>Business</dt><dd>Boxed and Blushing</dd>
      <dt>Where</dt><dd>South Africa (we deliver nationwide)</dd>
      <dt>WhatsApp and phone</dt><dd><a href="tel:+27643953029">064 395 3029</a></dd>
      <dt>Facebook</dt><dd><a href="https://www.facebook.com/profile.php?id=61585962997918" target="_blank" rel="noopener">Boxed and Blushing</a></dd>
      <dt>Website</dt><dd><a href="./">obsidianstudiodesigns.github.io/Boxed-and-Blushing</a></dd>
    </dl>"""

PAGES = {
    "privacy.html": dict(
        title="Privacy policy",
        desc="How Boxed and Blushing collects, uses and protects your personal information under the Protection of Personal Information Act (POPIA).",
        body=f"""
    <p class="lead">This policy explains how Boxed and Blushing ("we", "us") collects, uses and protects your personal information, in line with the Protection of Personal Information Act 4 of 2013 (POPIA).</p>

    <h2>Who we are</h2>
    {CONTACT}
    <p>The owner of Boxed and Blushing is our Information Officer under POPIA. Contact them on the details above about anything in this policy.</p>

    <h2>What we collect</h2>
    <p>We only collect the information you choose to give us when you order or ask a question, such as:</p>
    <ul>
      <li>your name and cellphone number (WhatsApp shares your number with us when you message us)</li>
      <li>the boxes and items you would like</li>
      <li>the names and roles you want printed on gifts, which may include the names of other people, such as your bridal party or a child</li>
      <li>your theme and colours, the date you need your order and your delivery town</li>
      <li>your delivery address when we arrange courier delivery</li>
      <li>anything else you include in your message</li>
    </ul>
    <p>If you give us someone else's name to print on a gift, please only share what is needed for the gift and make sure they would be happy with it. For gifts for children, a parent or guardian should place the order.</p>

    <h2>How the order form works</h2>
    <p>This website has no online shop, no payment system and no database. When you build an order, the boxes you add are remembered only in your own browser (local storage) so they are still there if you reload the page. The "Send my order on WhatsApp" button opens WhatsApp on your device with your order already written out. Nothing is sent to us unless you press send in WhatsApp yourself.</p>

    <h2>Why we use it</h2>
    <ul>
      <li>to quote for, make, personalise and deliver your order</li>
      <li>to answer your questions and keep you updated about your order</li>
      <li>to keep the records the law requires</li>
    </ul>
    <p>We do not sell, rent or trade your personal information, and we will not add you to any marketing list unless you ask us to.</p>

    <h2>Who we share it with</h2>
    <p>We only share your information when we need to, for example with a courier company so they can deliver your order, or when the law requires it. WhatsApp and Facebook (Meta) carry our messages under their own privacy policies.</p>

    <h2>Photos of our work</h2>
    <p>We like to share photos of finished boxes on Facebook and on this website. Personalised items may show a first name. If you would rather we did not share a photo of your order, just tell us when you order, or ask us to remove a photo at any time.</p>

    <h2>This website, cookies and third parties</h2>
    <p>This website does not set cookies and does not use analytics or advertising trackers. To load, your browser fetches files from these providers, which may record your IP address and browser details in their standard server logs:</p>
    <ul>
      <li>GitHub Pages, which hosts this website</li>
      <li>Google Fonts, which supplies the typefaces</li>
      <li>jsDelivr, which supplies the icons</li>
    </ul>
    <p>Links to WhatsApp and Facebook take you to services with their own privacy policies.</p>

    <h2>How long we keep it</h2>
    <p>We keep order messages only as long as we need them to make and deliver your order and handle any follow-up. Records of sales are kept for as long as tax law requires, usually five years, and then deleted.</p>

    <h2>How we protect it</h2>
    <p>We take reasonable steps to keep your information safe, including keeping it on password-protected devices and accounts and only sharing it when needed.</p>

    <h2>Your rights</h2>
    <p>Under POPIA you may:</p>
    <ul>
      <li>ask what personal information we hold about you</li>
      <li>ask us to correct or delete it</li>
      <li>object to us using it</li>
      <li>withdraw consent you have given</li>
    </ul>
    <p>Contact us on the details above and we will respond within a reasonable time. If you are unhappy with how we handle your information, you may complain to the Information Regulator of South Africa at <a href="https://inforegulator.org.za" target="_blank" rel="noopener">inforegulator.org.za</a>.</p>

    <h2>Changes to this policy</h2>
    <p>We may update this policy from time to time. The date at the top shows when it last changed.</p>
"""),
    "terms.html": dict(
        title="Terms of use",
        desc="Terms for using the Boxed and Blushing website and ordering personalised gift boxes: quotes, personalisation, payment, delivery, specials and returns.",
        body=f"""
    <p class="lead">These terms apply to this website and to orders placed through it or on WhatsApp. By using the website or sending us an order you agree to them.</p>

    <h2>About us</h2>
    <p>As required by section 43 of the Electronic Communications and Transactions Act 25 of 2002 (ECTA):</p>
    {CONTACT}
    <!-- TO CONFIRM with the client: owner's name, legal status (sole proprietor or company and registration number), physical address for legal notices, VAT number if registered -->

    <h2>Products and photos</h2>
    <p>Our boxes are made to order, so the exact items, colours and packaging can change with what is available and with your theme. Photos on this website show examples of past orders, and some lifestyle photos are styled or illustrative. If an item is out of stock we will offer you a similar one before we make your box.</p>

    <h2>Quotes and prices</h2>
    <p>Prices are in South African rand and are not listed on this website because every box is different. The price that applies is the one in the quote we send you on WhatsApp, including any delivery cost.</p>

    <h2>Placing an order</h2>
    <ul>
      <li>Sending us an order on WhatsApp is a request for a quote. Your order is only accepted once we confirm it in writing and any payment we agree on is received.</li>
      <li>Please check the spelling of every name, role and date you send us. We print exactly what you approve.</li>
      <li>Give us as much time as you can. We will tell you if we cannot make your date.</li>
    </ul>

    <h2>Payment</h2>
    <!-- TO CONFIRM with the client: accepted payment methods (EFT, cash, card) and deposit terms -->
    <p>Payment is made by the method and on the terms set out in your quote. We may ask for a deposit or full payment before we start on personalised items. We will never ask for your card details on WhatsApp.</p>

    <h2>Specials</h2>
    <p>Specials, such as our bridal party special, apply while they are advertised and to matching boxes in the same order. We confirm whether a special applies in your quote.</p>

    <h2>Delivery</h2>
    <p>We deliver across South Africa using a courier, at the cost in your quote. Delivery times are estimates from the courier. Please give us a full and correct address and a contact number, and tell us straight away if anything arrives damaged.</p>

    <h2>Changes, cancellations and returns</h2>
    <ul>
      <li>Personalised items are made just for you, so once we have started printing them we cannot cancel the order or accept a return because you changed your mind. This is allowed under section 42 of ECTA for goods made to your specifications.</li>
      <li>If you need to change or cancel an order before we start, tell us as soon as possible. Any deposit terms will be set out in your quote and will be fair and reasonable, as the Consumer Protection Act 68 of 2008 requires.</li>
      <li>If something is faulty, damaged or not what we agreed, tell us within 5 days of receiving it and we will repair, replace or refund it. Nothing in these terms limits your rights under the Consumer Protection Act.</li>
    </ul>

    <h2>Safety</h2>
    <p>Some boxes contain candles, glassware, alcohol or small items. Keep candles away from children and never leave them burning unattended. Alcohol is only included in orders for adults over 18. Baby and children's items are chosen with care, but please check every item before use and keep small parts away from babies.</p>

    <h2>Use of this website</h2>
    <p>The content, logo, photos and design of this website belong to Boxed and Blushing and its designers. You may not copy or reuse them without permission. We try to keep the information here correct and up to date, but we do not guarantee that it is complete or free of errors.</p>
    <p>This website links to WhatsApp, Facebook and other services. We are not responsible for their content or how they work.</p>

    <h2>Your information</h2>
    <p>How we handle personal information is set out in our <a href="privacy.html">privacy policy</a>.</p>

    <h2>Law</h2>
    <p>These terms are governed by the laws of the Republic of South Africa. Nothing in them limits your rights under the Consumer Protection Act or ECTA.</p>
"""),
}

for name, page in PAGES.items():
    cur = {k: "" for k in ("cur_privacy", "cur_terms")}
    cur["cur_" + name.split(".")[0]] = ' aria-current="page"'
    html = HEAD.format(title=page["title"], desc=page["desc"], base=BASE, wa=WA,
                       canonical=f'<link rel="canonical" href="{BASE}{name}">')
    html += f"""
  <main class="legal-main" id="main">
    <a class="back-link" href="./"><i class="ph ph-arrow-left" aria-hidden="true"></i> Back to Boxed and Blushing</a>
    <h1>{page["title"]}</h1>
    <p class="updated">Last updated: {UPDATED}</p>
{page["body"]}  </main>
"""
    html += FOOT.format(**cur)
    (ROOT / name).write_text(html, encoding="utf-8")

# 404
html = HEAD.format(title="Page not found", desc="This page could not be found. Head back to the Boxed and Blushing gift boxes.", base=BASE, wa=WA,
                   canonical='<meta name="robots" content="noindex">')
# GitHub Pages serves 404.html from any path, so links must be absolute.
html = html.replace('href="favicon', f'href="{BASE}favicon').replace('href="apple-touch', f'href="{BASE}apple-touch') \
           .replace('href="site.webmanifest"', f'href="{BASE}site.webmanifest"').replace('href="assets/', f'href="{BASE}assets/') \
           .replace('src="assets/', f'src="{BASE}assets/').replace('href="./', f'href="{BASE}')
html += f"""
  <main class="notfound" id="main">
    <div>
      <h1>404</h1>
      <p>This page is still being wrapped. The gift boxes are this way.</p>
      <a class="btn btn-primary" href="{BASE}#boxes">See the boxes</a>
    </div>
  </main>
"""
html += FOOT.format(cur_privacy="", cur_terms="").replace('href="privacy.html"', f'href="{BASE}privacy.html"') \
                                                  .replace('href="terms.html"', f'href="{BASE}terms.html"')
(ROOT / "404.html").write_text(html, encoding="utf-8")
print("pages written")
