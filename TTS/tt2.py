from PIL import Image
import pytesseract
from gtts import gTTS
import os

# Replace 'your_image.jpg' with the path to your image file
image_path = 'img1.jpg'

# Perform OCR on the image to extract text
text = pytesseract.image_to_string(Image.open('D:\KODIKON\img1.jpg'))

# Print the extracted text
print("Extracted Text:")
print(text)

# Convert the text to speech
tts = gTTS(text, lang='en')

# Save the speech to an audio file (e.g., 'output.mp3')
tts.save('output.mp3')

# Play the speech (requires an audio player)
os.system('start output.mp3')  # On Windows
# On Linux, you can use 'aplay output.mp3' or another audio player

# Alternatively, you can use a text-to-speech library to play the audio directly in your script
# For example, you can use the 'pyttsx3' library for text-to-speech:
# import pyttsx3
# engine = pyttsx3.init()
# engine.say(text)
# engine.runAndWait()
