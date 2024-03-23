import cv2
import numpy as np
from qreader import QReader

class QRCodeExtractionException(Exception):
    pass

class QRCodeExtractor:
    def __init__(self):
        self.image = None
        self.decoded_strings = None
        self.qreader = QReader()

    def decode(self, image_bytes):
        try:
            nparr = np.frombuffer(image_bytes, np.uint8)
            self.image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            self.decoded_strings = self.qreader.detect_and_decode(self.image)
        except Exception as e:
            raise QRCodeExtractionException(e)
        return self.decoded_strings