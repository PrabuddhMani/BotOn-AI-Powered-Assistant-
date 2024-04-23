import pyttsx3
import speech_recognition as sr
import re

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Adjust speaking rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Decrease speaking rate by 50 words per minute

def listen_for_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User Said: {query}")
        return query
    except Exception as e:
        print("Sorry, I couldn't understand. Please try again.")
        return ""

def speak(text):
    # Remove special symbols before speaking
    text = re.sub(r'[^\w\s]', '', text)
    engine.say(text)
    engine.runAndWait()
