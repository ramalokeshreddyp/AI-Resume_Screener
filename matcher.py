import json
import os
import re

def clean_text(text):
    # Lowercase, remove special characters
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    return text

def analyze_resume(resume_text, job_role):
    role_path = f"roles/{job_role.lower().replace(' ', '_')}.json"

    if not os.path.exists(role_path):
        return {
            "score": 0,
            "missing_skills": ["❌ Unknown job role. Add data in roles folder."],
            "certifications": [],
            "experiences": []
        }

    with open(role_path, 'r') as f:
        role_data = json.load(f)

    resume_text = clean_text(resume_text)

    found_skills = [skill for skill in role_data['skills'] if skill in resume_text]
    missing_skills = [skill for skill in role_data['skills'] if skill not in found_skills]

    score = int((len(found_skills) / len(role_data['skills'])) * 100)

    return {
        "score": score,
        "missing_skills": missing_skills,
        "certifications": role_data["certifications"],
        "experiences": role_data["experiences"]
    }
