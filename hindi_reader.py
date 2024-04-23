from googletrans import Translator
import pyttsx3

translator = Translator()
engine = pyttsx3.init()

def read_hindi_text(text):
    translated_text = translator.translate(text, src='hi', dest='en').text
    engine.say(translated_text)
    engine.runAndWait()
