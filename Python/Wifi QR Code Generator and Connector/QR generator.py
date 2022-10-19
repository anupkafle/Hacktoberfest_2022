
#generation of qr code for your wifi 

import qrcode
# import Image
id = "Wifi Name" #type your wifi name
password = 'Wifi_password' #Enter your wifi password here
# print(password)
qrcode = qrcode.QRCode()
qrcode.add_data(f"{id} {password}")
img = qrcode.make_image()
img.save("qr1.png")