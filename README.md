
# 🗺️ SkillStep

**SkillStep** is a personalized career roadmap generator built with Python and Streamlit.  
It helps students and aspiring professionals visualize the skills, courses, and projects they need to reach their career goals — based on what they already know and what they’re interested in.

---

## 🚀 Features

- 🎯 Select your degree, year, and career goal  
- 🧠 Add your interests and current skills  
- 🤖 Gemini-powered dynamic roadmap generation *(new)*  
- 📚 Automatically generates a step-by-step skill learning path  
- 🛠️ Recommends projects and free learning resources  
- ⚡ Simple and clean Streamlit web interface  

---

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)  
- **Backend Logic:** Python  
- **AI Integration:** [Gemini 1.5 Flash](https://ai.google.dev) via `google-generativeai`  
- *(Legacy)* `templates.json` for static roadmaps  
- *(Optional)* Udemy API integration for course suggestions  

---

## 🤖 Gemini API Integration

SkillStep uses **Google’s Gemini 1.5 Flash model** to generate short, goal-specific learning roadmaps based on:

- Your career goal (e.g. *Data Scientist*)
- Your current skills (e.g. *Python, SQL*)
- Your areas of interest (e.g. *AI, Web Dev*)

Each roadmap step includes:
- A **skill to learn**
- A **mini project** to apply it
- A **free course/tutorial** suggestion

### 🔐 To use Gemini:
1. Create a `.env` file in the project root  
2. Add your API key:
   ```env
   GEMINI_API_KEY=your_api_key_here


---

## 📁 Project Structure

```
skillstep/
├── app.py                # Streamlit frontend
├── roadmap_generator.py  # Timeline generation logic (Gemini integrated)
├── templates.json        # Static templates (fallback)
├── test_api.py           # Model access tester (optional)
├── .env                  # Gemini API key (excluded from Git)
└── README.md             # Project documentation
```

---

## 🧪 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/arshaimran/SkillStep.git
cd SkillStep
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # on Windows
source venv/bin/activate   # on Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 If you don’t have `requirements.txt`, just run:

```bash
pip install streamlit google-generativeai python-dotenv
```

### 4. Set Up Your `.env`

Create a `.env` file in the project root with your Gemini API key:

```env
GEMINI_API_KEY=your_actual_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🌱 Example Career Goals

* Data Scientist
* Web Developer
* AI Researcher
* Product Manager
* UX Designer

---

## 📌 Roadmap Output Format (Gemini-powered)

```
Step 1: Learn Python Basics  
🛠 Project: Build a calculator  
📚 Resource: "Python for Beginners" – freeCodeCamp

Step 2: Learn SQL  
🛠 Project: Build a student database  
📚 Resource: "Intro to SQL" – Mode Analytics
...
```

---

## 💡 Future Improvements

* 🔄 Dynamic course suggestions from Udemy or Coursera APIs
* 💾 Export roadmap as PDF or save user progress
* 🎨 Visualize roadmap using timeline charts or skill graphs
* 👥 Add multi-user login (educators, students, etc.)

---

## 👩‍💻 Author

Made with ❤️ by [Arsha Imran](https://github.com/arshaimran)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

````

---

