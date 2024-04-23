import pyttsx3
import datetime
import speech_recognition as sr
import requests
import re

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Adjust speaking rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Decrease speaking rate by 50 words per minute

input_preference = 'text'  # Default preference


def speak(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove special symbols
    engine.say(text)
    engine.runAndWait()


def chat_with_generative_language(query):
    api_key = "YOUR_GENERATIVE_API_KEY"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{
            "parts": [{
                "text": query
            }]
        }]
    }
    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}",
        headers=headers, json=data)
    try:
        response_json = response.json()
        if "candidates" in response_json and response_json["candidates"]:
            return response_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Error: Unexpected response format from API."
    except Exception as e:
        return f"Error: {e}"


def take_input():
    global input_preference
    if input_preference == 'text':
        query = input("You: ")
        return query
    elif input_preference == 'voice':
        speak("Please say your query.")
        query = listen_for_voice_input()
        return query


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


def update_program():
    # Code to update the program
    pass  # Placeholder, replace with actual code


if __name__ == "__main__":
    speak("Good Evening!")
    speak("Hi, please tell me how may I help you?")
    speak("Do you want to give commands in voice or text?")
    while True:
        response = listen_for_voice_input()
        response = response.lower()
        if response == 'voice' or response == 'text':
            input_preference = response
            break
        else:
            speak("Invalid input. Please enter 'voice' or 'text'.")

    while True:
        query = take_input()
        if query:
            if "update your program" in query:
                update_program()
                speak("Program updated successfully.")
                continue
            response_text = chat_with_generative_language(query)
            print("AI:", response_text)
            if not re.match(r'^[_\W]+$', response_text):
                speak(response_text[:200])  # Speak only the first 200 characters
