# -*- coding:utf-8 -*-
from PIL import Image
import pytesseract

image = Image.open("1.png")
image.load()

imgry = image.convert('L')

print pytesseract.image_to_string(imgry)




