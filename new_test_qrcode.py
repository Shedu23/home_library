import pyqrcode
import qrcode
#import os


def generate_qr():
    for i in range(1, 5):
        img_name = "Шкаф 1, ряд : " + str(i)
        print(img_name)
        img = qrcode.make(img_name)
        img_name = img_name + '.png'
        img.save(img_name)

if __name__ == '__main__':
    generate_qr()