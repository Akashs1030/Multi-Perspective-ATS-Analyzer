# 📄 ATS Resume Expert — AI Resume Analyzer

An AI-powered **ATS Resume Analysis application** that compares a resume with a job description using **Google Gemini** and provides recruiter-style feedback, skill-gap analysis, missing keywords, and a resume-to-job match score.

## 🚀 Features

* 📄 Upload resume in PDF format
* 📝 Enter a target job description
* 🧑‍💼 AI-powered resume analysis
* 📈 Identify skill gaps and improvement areas
* 🔍 Find missing ATS keywords
* 🎯 Calculate resume-to-job match percentage
* 🎨 Interactive Streamlit interface
* 🤖 Google Gemini-powered analysis

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini (`gemini-3.5-flash`)**
* **PyPDF2 / PDF processing**
* **pdf2image**
* **Pillow**
* **python-dotenv**

## 🔄 Workflow

```text
Resume PDF + Job Description
            ↓
       PDF → Image
            ↓
       Gemini Vision
            ↓
    AI Resume Analysis
            ↓
 ┌──────────┼──────────┐
 ↓          ↓          ↓
Resume    Skill      Missing
Review    Gaps      Keywords
            ↓
       Match Score
```

## 📊 Analysis Options

The application provides four analysis modes:

1. **Resume Overview** — Recruiter-style resume analysis
2. **Skill Improvement** — Identifies existing and missing skills
3. **Missing Keywords** — Finds relevant ATS keywords absent from the resume
4. **Percentage Match** — Calculates resume-to-job-description match

These four actions are directly implemented in the application UI.

## ⚙️ Installation

```bash
git clone <YOUR_REPOSITORY_URL>
cd ATS-Resume-Expert
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

## ▶️ Run

```bash
streamlit run app.py
```

## 🔮 Future Improvements

* Resume scoring dashboard
* Resume improvement suggestions
* Multiple resume comparison
* Job recommendation system
* Resume keyword visualization
* Downloadable analysis reports
