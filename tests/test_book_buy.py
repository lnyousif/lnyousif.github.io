"""Offline checks for the curated buying page. Run: python -m unittest discover -s tests."""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements = []
        self.retailer_groups = {}
        self._retailer_group = None
        self._retailer_link = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag == 'ul' and 'retailers' in attrs.get('class', '').split():
            self._retailer_group = attrs.get('aria-labelledby')
            self.retailer_groups[self._retailer_group] = []
        elif tag == 'a' and self._retailer_group:
            self._retailer_link = [attrs['href'], []]

    def handle_data(self, data):
        if self._retailer_link is not None:
            self._retailer_link[1].append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self._retailer_link is not None:
            href, chunks = self._retailer_link
            label = ' '.join(chunk.strip() for chunk in chunks if chunk.strip())
            self.retailer_groups[self._retailer_group].append((href, label))
            self._retailer_link = None
        elif tag == 'ul':
            self._retailer_group = None


class BookBuyTest(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / 'buy/index.html').read_text()
        self.page = Page(self.text)

    def test_identifies_correct_book_and_format(self):
        for value in ['Baghdad to Brooklyn', 'An Ordinary Journey Through Extraordinary Times',
                      'Laith Yousif', '9798950391057', 'Paperback', 'Manhattan Book Group']:
            self.assertIn(value, self.text)
        self.assertNotIn('Kindle', self.text)
        self.assertNotIn('Audiobook', self.text)

    def test_exact_curated_retailers_no_tracking(self):
        links = [attrs['href'] for tag, attrs in self.page.elements if tag == 'a']
        external = [u for u in links if u.startswith('https:') and 'laithyousif.com' not in u]
        expected = {
            'https://www.amazon.com/dp/B0HHG9M6J1',
            'https://www.thriftbooks.com/w/baghdad-to-brooklyn-an-ordinary-journey-through-extraordinary-times_laith-yousif/60282703/',
            'https://tertulia.com/book/baghdad-to-brooklyn-an-ordinary-journey-through-extraordinary-times-laith-yousif/9798950391057',
            'https://www.lafeltrinelli.it/baghdad-to-brooklyn-ordinary-journey-libro-inglese-laith-yousif/e/9798950391057',
            'https://preigu.de/buecher/baghdad-to-brooklyn/136459812',
            'https://www.orellfuessli.ch/shop/home/artikeldetails/A1081550450',
        }
        self.assertEqual(len(external), len(expected))
        self.assertEqual(set(external), expected)
        self.assertTrue(all(not urlparse(u).query and not urlparse(u).fragment for u in external))

    def test_retailer_groups_have_named_lists_and_explicit_countries(self):
        groups = self.page.retailer_groups
        self.assertEqual(list(groups), ['retailers-us', 'retailers-europe'])
        for group in groups:
            self.assertIn(('h3', {'id': group}), self.page.elements)
        self.assertIn('<h3 id="retailers-us">United States</h3>', self.text)
        self.assertIn('<h3 id="retailers-europe">Europe</h3>', self.text)
        self.assertEqual(
            [(urlparse(url).netloc, label) for url, label in groups['retailers-us']],
            [('www.amazon.com', 'Amazon View paperback →'),
             ('www.thriftbooks.com', 'ThriftBooks View paperback →'),
             ('tertulia.com', 'Tertulia View paperback →')],
        )
        self.assertEqual(
            [(urlparse(url).netloc, label) for url, label in groups['retailers-europe']],
            [('www.lafeltrinelli.it', 'Feltrinelli (Italy) View English paperback →'),
             ('preigu.de', 'preigu (Germany) View English paperback →'),
             ('www.orellfuessli.ch', 'Orell Füssli (Switzerland) View English paperback →')],
        )

    def test_retailers_leave_price_delivery_and_availability_to_sellers(self):
        self.assertIn('Check the retailer for current price, delivery and availability in your country.', self.text)
        self.assertIn('Prefer your local bookstore? Ask whether they can order the paperback using the ISBN above.', self.text)
        self.assertIn('href="/excerpt/"', self.text)
        self.assertNotIn('In stock', self.text)
        self.assertNotIn('€', self.text)

    def test_accessible_structure_and_no_script_requirement(self):
        tags = [tag for tag, _ in self.page.elements]
        self.assertEqual(tags.count('h1'), 1)
        self.assertEqual(tags.count('main'), 1)
        self.assertNotIn('script', tags)
        self.assertIn(('html', {'lang': 'en'}), self.page.elements)
        self.assertIn('href="#book"', self.text)
        self.assertIn('id="book"', self.text)
        for tag, attrs in self.page.elements:
            if tag == 'img':
                self.assertTrue(attrs.get('alt'))
                self.assertTrue((ROOT / attrs['src'].lstrip('/')).exists())

    def test_share_url_metadata_and_local_assets(self):
        self.assertIn('rel="canonical" href="https://www.laithyousif.com/buy/"', self.text)
        self.assertIn('name="viewport"', self.text)
        self.assertTrue((ROOT / 'assets/css/book-buy.css').exists())
        css = (ROOT / 'assets/css/book-buy.css').read_text()
        self.assertIn('@media (max-width: 600px)', css)
        self.assertIn(':focus-visible', css)

    def test_entry_points_and_evergreen_ctas(self):
        home = (ROOT / 'index.html').read_text()
        press = (ROOT / 'press/index.html').read_text()
        self.assertIn("'/buy/' | relative_url", home)
        self.assertEqual(press.count('href="/buy/"'), 2)
        self.assertNotIn('especially around the 25th anniversary', home)
        self.assertNotIn('Press resources for the 25th anniversary', press)
        self.assertNotIn('https://a.co/d/01NEp0rj', press)


if __name__ == '__main__':
    unittest.main()
