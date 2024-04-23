from googletrans import Translator

def detect_language(text):
    translator = Translator()
    try:
        result = translator.detect(text)
        if result:
            return result.lang
        else:
            return "en"  # Default to English if result is None
    except Exception as e:
        print("Error detecting language:", e)
        return "en"  # Default to English in case of error

def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, dest='hi')
    return translation.text

def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text
