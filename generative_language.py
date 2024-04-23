# generative_language.py

import requests

def chat_with_generative_language(query, api_key):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": query}]}]}
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
