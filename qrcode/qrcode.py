# install pyqrcode
# pip install pyqrcode

import pyqrcode
from pyqrcode import QRCode

# string which represent the QR code
s = "https://www.youtube.com/watch?v=gomDSZaay3E"

# Generate QR code
url = pyqrcode.create(s)

# Create an save the png file naming "myyoutube.svg"
url.svg("myyoutube.svg", scale=8)
