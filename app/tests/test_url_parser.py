import unittest
from ..parser import URLParser

class TestURLParser(unittest.TestCase):
    def test_parse_urls(self):
        parser = URLParser()
        entries = ["https://qrco.de/beuVsn", "https://broken/beuVsn"]
        results = parser.parse_urls(entries)
        
        self.assertEqual(len(results['urls']), 2)
        
        first_entry = results['urls'][0]
        self.assertEqual(first_entry['netloc'], 'qrco.de')
        self.assertNotIn('ip_error', first_entry)
        
        second_entry = results['urls'][1]
        self.assertEqual(second_entry['netloc'], 'broken')
        self.assertIn('ip_error', second_entry)

if __name__ == '__main__':
    unittest.main()
