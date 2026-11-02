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
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


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
        self.assertEqual(len(external), 3)
        self.assertEqual({urlparse(u).netloc for u in external},
                         {'www.amazon.com', 'www.thriftbooks.com', 'tertulia.com'})
        self.assertTrue(all(not urlparse(u).query for u in external))
        self.assertIn('https://www.amazon.com/dp/B0HHG9M6J1', external)

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
