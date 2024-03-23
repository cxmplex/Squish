from bottle import Bottle, request, HTTPError, static_file
from squish.parser import QRCodeExtractor, QRCodeExtractionException
from squish.processor import URLParser, URLParserException

import json

app = Bottle()

@app.route('/')
def serve_index():
    return static_file('index.html')

@app.route('/submit', method='POST')
def submit():
    upload = request.files.get('image')
    if not upload:
        return HTTPError(400, "File not found.")
    
    # get bytes from image
    image_bytes = upload.file.read()
    if len(image_bytes) == 0:
        return HTTPError(400, "Image is empty.")

    # extract qr code and contents from image
    extractor = QRCodeExtractor()
    try:
        extracted_strings = extractor.decode(image_bytes)
    except QRCodeExtractionException as e:
        return json.dumps({"error": str(e)})

    # parse the url
    parser = URLParser()
    results = None

    try:
        results = parser.parse_urls(extracted_strings)
    except URLParserException as e:
        return json.dumps(results,indent=4)

    if not results:
        return "No URLS were found, extraction results: {}".format(extracted_strings)
    
    # return json results
    return json.dumps(results,indent=4)
