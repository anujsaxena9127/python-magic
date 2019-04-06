import pytesseract
from PIL import Image
from gtts import gTTS
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = Image.open('index.png')
result= pytesseract.image_to_string(img)
print(result)
text="This is the first line of this text example.This is the second line of the same text."
speech=gTTS(text,'en','slow')
speech.save("hello3.mp3")