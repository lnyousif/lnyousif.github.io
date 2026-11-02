# Book buying page

`/buy/` is the stable, script-free link-in-bio destination. The homepage and press
kit link here. The new URL becomes live only after the PR is merged and Pages
publishes it; creating the PR does not deploy it.

## Curated listings

Checked November 2, 2026, against the title and author (and paperback ISBN
9798950391057 where exposed). No affiliate tags, prices, stock promises, or
review scores are stored on the page.

- Amazon: https://www.amazon.com/dp/B0HHG9M6J1 — author's existing canonical print link; verified exact product in prior browser check.
- ThriftBooks: https://www.thriftbooks.com/w/baghdad-to-brooklyn-an-ordinary-journey-through-extraordinary-times_laith-yousif/60282703/ — live HTTP 200 listing; matching title/author/ISBN, paperback.
- Tertulia: https://tertulia.com/book/baghdad-to-brooklyn-an-ordinary-journey-through-extraordinary-times-laith-yousif/9798950391057 — official indexed listing matches title/author/ISBN and paperback. Direct automated request returned 403; checkout was not tested.

Only the verified paperback listings are offered. No unverified B&N, Bookshop,
ebook or audiobook URLs are invented. Retailer availability and delivery can
change and should be checked on the retailer's site. To add a format, verify the
actual edition and direct listing first, then update `buy/index.html` and the
curated-link test. Do not substitute similarly titled books by other authors.

## Checks

- `python -m unittest discover -s tests -v` checks identity, exact retailer hosts,
  metadata, navigation, responsive/focus CSS hooks and no JavaScript dependency.
- `bash tools/test.sh` is the repository's full Jekyll build + html-proofer check
  and requires Ruby/Bundler from the existing Gemfile.
- Manually check `/buy/` at narrow and wide widths and keyboard navigation when a
  browser is available. The new page is plain HTML/CSS, like the press page.
