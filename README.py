# This is using of Vs code and extension library install Qrcode
# Generate Qr-code and URL link uses in input
# No internet needs because without internet generate Qrcode in link.
# File location address needs to be stored in file locate.

import qrcode

url = input('Enter a URL:').strip()
fp = 'C:\\Users\DELL\\OneDrive\\Desktop\\qrcode.png'

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(fp)

