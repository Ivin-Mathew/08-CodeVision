import pytesseract
from PIL import Image

def image_to_text():
    image = Image.open("C:\\Users\\ivinm\\github\\08-CodeVision\\TTS")
    text = pytesseract.image_to_string(image)
    print (text)
