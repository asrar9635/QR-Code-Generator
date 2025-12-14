import qrcode

url = input('Enter a URL:').strip()
fp = 'C:\\Users\DELL\\OneDrive\\Desktop\\qrcode.png'

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(fp)
