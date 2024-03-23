# Squish
Squish quishing (QR code based phishing) with ease

Fun 1 hour code-write for QR-code detection, URL extraction, URL processing.

# Demo

Hosted on Amazon Web Services EC2

# Building

Squish is a dockerized application. Building and running it is as simple as:

`docker build -t squish .`

`docker run -p 8085:8085 squish`

# Features

Image Attachment (PNG) Submission via API

QR Code detection powered by QReader

URL Extraction from QR code

URL processing (whois, domain, tld, ip, subdirectories, etc)


Third Party Libraries:

QReader - QReader is a Robust and Straight-Forward solution for reading difficult and tricky QR codes within images in Python. Powered by a YOLOv8 model.

bottle - Extremely simple and lightweight web server wrapper (great for demos!)

gunicorn - The actual http server that bottle is wrapping

