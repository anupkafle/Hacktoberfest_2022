import os
from pyzbar.pyzbar import decode
# from PIL import Image
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
bol=True
while bol:
    bol, img = cap.read()
    # db = decode(Image.open('qr1.png'))
    db= decode(img)
    for data in db:
        id, password = data.data.decode("utf-8").split()
        os.system(f'cmd /с "netsh wlan set hostednetwork mode=allow ssid={id} key={password}"')
        os.system(f'cmd /с "netsh wlan connect ssid={id} name={id}"')
    cv2.imshow("output", img)
    cv2.waitKey(1)