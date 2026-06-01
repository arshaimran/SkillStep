import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_timeline_with_gemini(goal, interests, current_skills):
    prompt = f"""
I am a student and want to become a {goal}.  
Here are my current skills: {current_skills}.  
These are the areas I'm interested in: {', '.join(interests)}.

Please create a **concise, numbered roadmap (5–7 steps)** that will prepare me to become a {goal}.

Each step must include:
- One specific skill to learn
- A simple, related project idea
- A **free course/tutorial** recommendation (with the platform name)

The format should be:
Step 1: Learn [Skill]  
🛠 Project: [Project idea]  
📚 Resource: [Course name] – [Platform]

Make sure the steps build up to help me confidently achieve my goal.
Avoid long paragraphs or extra text.
"""

    model = genai.GenerativeModel(model_name="gemini-1.5-flash") 
    response = model.generate_content(prompt)
    return response.text
