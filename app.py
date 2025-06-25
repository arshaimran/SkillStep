from roadmap_generator import load_templates, generate_timeline
import streamlit as st

st.set_page_config(page_title="SkillStep", layout="centered")
st.title("🗺️ SkillStep")

st.markdown("Create your personalized career roadmap, tailored to your current skills and future goals — one step at a time.")


with st.form("user_form"):
    name = st.text_input("Your Name")
    degree = st.selectbox("Degree Program", ["BS Data Science", "BS CS", "BBA", "Engineering", "Other"])
    year = st.selectbox("Current Year", ["1st", "2nd", "3rd", "Final"])
    goal = st.selectbox("Career Goal", ["Data Scientist", "Web Developer", "AI Researcher", "Product Manager", "UX Designer"])
    interests = st.multiselect("What are you interested in?", ["AI", "Machine Learning", "Web Dev", "UI/UX", "Cloud", "Data Analytics"])
    current_skills = st.text_area("Skills you already know (comma-separated)", placeholder="e.g., Python, SQL, Excel")

    submitted = st.form_submit_button("Generate Timeline")

if submitted:
    st.success(f"✅ Thanks {name}! Here's your personalized roadmap:")
    templates = load_templates()
    timeline = generate_timeline(goal, interests, current_skills, templates)

    for step in timeline:
        st.markdown(f"---\n{step}")



