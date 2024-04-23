import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use index 0 for English voice and index 1 for Hindi voice

def speak(text, lang):
    if lang == 'hi':
        engine.setProperty('voice', voices[1].id)  # Use Hindi voice
    else:
        engine.setProperty('voice', voices[0].id)  # Use English voice
    engine.say(text)
    engine.runAndWait()
