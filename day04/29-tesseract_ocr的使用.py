import pytesseract
from PIL import Image

img = Image.open('yzm1.png')
code = pytesseract.image_to_string(img)
print(code)