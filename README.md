# AI-Resume_Screener
# 🧠 AI Resume Screener – Smart Resume Analyzer using NLP

**AI Resume Screener** is a Python-powered web app that uses **Natural Language Processing (NLP)** to evaluate resumes against a **target job role** and provide intelligent feedback:

- ✅ Resume Match Score (out of 100)
- ❌ Missing Skills
- 📜 Recommended Certifications
- 💼 Suggested Projects or Experience

Built using **Flask**, **PyPDF2**, and **custom role datasets**, it helps job seekers understand how well their resume aligns with their dream job — and how to improve it!

---

## 🚀 Features

- 📄 Upload a PDF Resume
- 🎯 Specify a target job role (e.g. "Data Analyst")
- 📊 Get a Resume Score out of 100
- 🧠 Smart analysis of:
  - ✅ Existing vs. Missing Skills
  - 📜 Recommended Certifications
  - 💼 Experience Suggestions
- 💡 Dynamic and Beautiful Interface (Jinja + CSS)
- 🔧 Easily extend with new job roles in `roles/*.json`

---

## 🛠️ Tech Stack

### 💻 Frontend
- **HTML5**
- **CSS3**
- **Jinja2 (Flask Templating)**

### 🧠 Backend
- **Python 3.8+**
- **Flask** – lightweight backend framework
- **PyPDF2** – for extracting text from resumes (PDFs)
- **Custom NLP Logic** – for resume analysis
- **JSON Files** – for job-role-based skill data

---

## 📁 Project Structure

resume-screener/
│
├── app.py # Main Flask app
├── requirements.txt # Python dependencies
│
├── utils/
│ ├── parser.py # PDF parser logic
│ └── matcher.py # Resume analysis logic
│
├── roles/ # Pre-defined job role data
│ ├── data_analyst.json
│ ├── data_scientist.json
│ ├── ml_engineer.json
│ └── web_developer.json
│
├── templates/
│ └── index.html # Frontend (Jinja)
│
└── static/ # Optional styles/scripts (if needed)
