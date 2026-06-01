import streamlit as st
import os
from dotenv import load_dotenv
from roadmap_generator import generate_timeline_with_gemini

# Load Gemini API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="SkillStep", layout="centered")
st.title("🗺️ SkillStep")

st.markdown("""
Welcome to **SkillStep** — your personalized career roadmap generator!  
Enter your academic background, interests, and current skills to get a step-by-step roadmap with learning resources and project suggestions.
""")

with st.form("user_form"):
    st.subheader("👤 Your Info")
    name = st.text_input("Your Name")

    st.subheader("🎓 Academic Background")
    degree = st.selectbox("Degree Program", ["", "BS Data Science", "BS Computer Science", "BS Software Engineering", "Other"])

    year = st.selectbox("Current Year", ["", "1st", "2nd", "3rd", "Final"])

    st.subheader("🚀 Career Path")
    goal = st.selectbox("Career Goal", ["", "Data Scientist", "Web Developer", "AI Researcher", "Product Manager", "UX Designer"])

    interests = st.multiselect("What are you interested in?", ["AI", "Machine Learning", "Web Dev", "UI/UX", "Cloud", "Data Analytics"])

    st.subheader("🧠 Your Skills")
    current_skills = st.text_area("Skills you already know (comma-separated)", placeholder="e.g., Python, SQL, Excel")

    submitted = st.form_submit_button("Generate Roadmap")

# Validate input
if submitted:
    if not name.strip():
        st.error("❗ Please enter your name.")
    elif not degree:
        st.error("❗ Please select your degree.")
    elif not year:
        st.error("❗ Please select your year.")
    elif not goal:
        st.error("❗ Please select a career goal.")
    elif not interests:
        st.error("❗ Please select at least one interest.")
    else:
        st.success(f"✅ Thanks {name}! Here's your personalized roadmap:")
        timeline = generate_timeline_with_gemini(goal, interests, current_skills)

        
    st.markdown(timeline)
