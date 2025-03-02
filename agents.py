import google.generativeai as genai
from config import get_gemini_api_key

def create_agent():
    genai.configure(api_key=get_gemini_api_key())
    model = genai.GenerativeModel("gemini-1.5-flash")  # Free model
    return model

def get_recommendations(agent, user_profile):
    response = agent.generate_content(user_profile)
    return response.text if response else "No response generated."

def get_fitness_plan(agent, user_profile):
    return get_recommendations(agent, user_profile)

def get_dietary_plan(agent, user_profile):
    return get_recommendations(agent, user_profile)
