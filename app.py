from flask import Flask, render_template, request
import os
from utils.parser import extract_text_from_pdf
from utils.matcher import analyze_resume
import uuid

app = Flask(__name__)

# Set where resumes will be temporarily stored
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        # Get job role and resume from form
        job_role = request.form['job_role']
        resume_file = request.files['resume']

        if resume_file and resume_file.filename.endswith('.pdf'):
            # Generate unique filename and save file
            filename = f"{uuid.uuid4().hex}.pdf"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume_file.save(filepath)

            # Extract resume text
            resume_text = extract_text_from_pdf(filepath)

            # Analyze resume using matcher
            result = analyze_resume(resume_text, job_role)

            # Remove file after analysis
            os.remove(filepath)
        else:
            result = {
                "score": 0,
                "missing_skills": ["❌ Invalid file format. Please upload a PDF."],
                "certifications": [],
                "experiences": []
            }

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
