#import PyQRCode
import pyqrcode

for i in range(1,11):
    img_name = "The book number id is : " + str(i)
    print(img_name)
    img_name = img_name + '.svg'
    img = pyqrcode.create(img_name)
    img.svg(img_name, scale=4)

    #img = pyqrcode.create('OIEB')
    #img.svg('text1.svg', scale=2)
    #img2 = pyqrcode.create('Igor Sharov')
    #img2.svg('text2.svg', scale=2)

'''
>>> import pyqrcode
>>> url = pyqrcode.create('http://uca.edu')
>>> url.svg('uca-url.svg', scale=8)
>>> url.eps('uca-url.eps', scale=2)
>>> print(url.terminal(quiet_zone=1))
'''
