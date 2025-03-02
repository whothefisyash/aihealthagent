import os
import google.generativeai as genai

def get_gemini_api_key():
    return os.getenv("GEMINI_API_KEY")  # Ensure this is set in the environment

def set_gemini_api_key(key):
    os.environ["GEMINI_API_KEY"] = key
    genai.configure(api_key=key)