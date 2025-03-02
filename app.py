import streamlit as st
from config import get_gemini_api_key, set_gemini_api_key
from agents import create_agent, get_fitness_plan, get_dietary_plan

def main():
    st.title("AI Health & Fitness Planner")
    
    # API Key Input
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    if api_key:
        set_gemini_api_key(api_key)
    
    # User Input Fields
    st.sidebar.header("User Information")
    age = st.sidebar.number_input("Age", min_value=1, max_value=120, step=1)
    weight = st.sidebar.number_input("Weight (kg)", min_value=10, max_value=200, step=1)
    height = st.sidebar.number_input("Height (cm)", min_value=50, max_value=250, step=1)
    activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
    goal = st.sidebar.selectbox("Goal", ["Lose Weight", "Maintain Weight", "Gain Muscle"])
    dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., Vegan, Keto)")

    user_profile = f"Age: {age}, Weight: {weight}, Height: {height}, Activity: {activity_level}, Goal: {goal}, Diet: {dietary_preferences}"
    
    agent = create_agent()
    
    if st.button("Generate Fitness Plan"):
        fitness_plan = get_fitness_plan(agent, user_profile)
        st.success(fitness_plan)
    
    if st.button("Generate Dietary Plan"):
        dietary_plan = get_dietary_plan(agent, user_profile)
        st.success(dietary_plan)
