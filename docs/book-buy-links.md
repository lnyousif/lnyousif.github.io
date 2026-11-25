# Book buying page

`/buy/` is the stable, script-free link-in-bio destination. The homepage and press
kit link here. Changes to the page reach the live URL only after the PR is merged and Pages
publishes them; creating the PR does not deploy them.

## Curated listings

### United States

Checked November 2, 2026, against the title and author (and paperback ISBN
9798950391057 where exposed). No affiliate tags, prices, stock promises, or
review scores are stored on the page.

- Amazon: https://www.amazon.com/dp/B0HHG9M6J1 — author's existing canonical print link; verified exact product in prior browser check.
- ThriftBooks: https://www.thriftbooks.com/w/baghdad-to-brooklyn-an-ordinary-journey-through-extraordinary-times_laith-yousif/60282703/ — live HTTP 200 listing; matching title/author/ISBN, paperback.
- Tertulia: https://tertulia.com/book/baghdad-to-brooklyn-an-ordinary-journey-through-extraordinary-times-laith-yousif/9798950391057 — official indexed listing matches title/author/ISBN and paperback. Direct automated request returned 403; checkout was not tested.

### Europe

Checked November 25, 2026, against each retailer's direct product page. All
three identify the matching title, Laith Yousif, English paperback, Manhattan
Book Group, and ISBN/EAN 9798950391057.

- **Italy — Feltrinelli:** https://www.lafeltrinelli.it/baghdad-to-brooklyn-ordinary-journey-libro-inglese-laith-yousif/e/9798950391057 — product details identify English text, paperback/softback, and EAN 9798950391057.
- **Germany — preigu:** https://preigu.de/buecher/baghdad-to-brooklyn/136459812 — product details identify an English paperback (Taschenbuch), ISBN-13 9798950391057, and item 136459812.
- **Switzerland — Orell Füssli:** https://www.orellfuessli.ch/shop/home/artikeldetails/A1081550450 — product details identify English (Englisch), paperback (Taschenbuch), and EAN 9798950391057.

The country labels identify retailer markets, not exclusive delivery areas or
translated editions. Listing identity does not establish stock, price, checkout
success, shipping, or sales; no such claims are made on the page.

Only the verified paperback listings are offered. No unverified B&N, Bookshop,
ebook or audiobook URLs are invented. Retailer availability and delivery can
change and should be checked on the retailer's site. To add a format, verify the
actual edition and direct listing first, then update `buy/index.html` and the
curated-link test. Do not substitute similarly titled books by other authors.

## Checks

- `python -m unittest discover -s tests -v` checks identity, exact curated URLs,
  region/country labels, metadata, navigation, responsive/focus CSS hooks and no
  JavaScript dependency.
- `bash tools/test.sh` is the repository's full Jekyll build + html-proofer check
  and requires Ruby/Bundler from the existing Gemfile.
- Manually check `/buy/` at narrow and wide widths and keyboard navigation when a
  browser is available. The new page is plain HTML/CSS, like the press page.
