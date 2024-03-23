import unittest
from ..parser import QRCodeExtractor

class TestQRCodeExtractorFunctionality(unittest.TestCase):

    def test_decode_qr_code(self):
        test_image_path = 'test.png'
        
        extractor = QRCodeExtractor()

        with open(test_image_path, 'rb') as image_file:
            image_bytes = image_file.read()
        
        decoded_strings = extractor.decode(image_bytes)
        
        self.assertIn("https://qrco.de/beuVsn", decoded_strings)

if __name__ == '__main__':
    unittest.main()