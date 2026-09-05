# ResumeSense – Multi-Perspective ATS Analyzer

ResumeSense is an AI-powered resume analysis tool that evaluates resumes against job descriptions using **Google Gemini's vision capabilities**. Instead of relying on error-prone text extraction, it converts resumes directly into image input for the LLM, preserving layout and formatting context during analysis.


## ✨ Features

* **Multi-mode analysis** — four distinct evaluation modes in a single app:

  * 🧑‍💼 **Tell Me About the Resume** — recruiter-style overview of candidate profile, strengths, and notable projects
  * 📈 **How Can I Improve My Skills** — career-coach feedback identifying underdeveloped skills and actionable growth steps
  * 🔍 **What Are the Keywords That Are Missing** — ATS-optimization scan comparing the resume against a job description for missing hard and soft skills
  * 🎯 **Percentage Match** — weighted job-description match score:

    * Skills — 40%
    * Experience — 20%
    * Keyword Overlap — 25%
    * Domain Relevance — 15%

* **Vision-based parsing** — resumes are converted to images and analyzed directly by Gemini, helping preserve formatting and layout context.

* **Specialized prompt engineering** — each analysis mode uses a purpose-built prompt designed for a specific evaluation behavior.

* **Polished UI** — custom-styled Streamlit interface with sidebar guidance, gradient hero header, and animated result cards.

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **LLM:** Google Gemini Vision via `google-generativeai`
* **PDF Processing:** `pdf2image`, `Pillow (PIL)`
* **Environment Management:** `python-dotenv`

## 🔄 How It Works

```text
Resume PDF + Job Description
            ↓
      PDF → Image
            ↓
     Select Analysis Mode
            ↓
 Specialized Gemini Prompt
            ↓
     Gemini Vision Analysis
            ↓
       AI-Generated Report
```

1. User pastes a job description and uploads a resume in PDF format.
2. The first page of the resume is converted into a JPEG image.
3. User selects one of the four analysis modes.
4. The corresponding prompt and resume image are sent to Gemini.
5. Gemini analyzes the resume and generates the requested evaluation.
6. The result is displayed through the Streamlit interface.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd resumesense
```

### 2. Install dependencies

```bash
pip install streamlit google-generativeai pdf2image pillow python-dotenv
```

### 3. Install Poppler

`pdf2image` requires Poppler for PDF processing.

**Windows:** Download Poppler binaries and add them to your system PATH.

**macOS:**

```bash
brew install poppler
```

**Linux:**

```bash
sudo apt-get install poppler-utils
```

### 4. Configure your Gemini API key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

## 📖 Usage

1. Paste the target job description into the text area.
2. Upload your resume as a PDF.
3. Select an analysis mode:

   * Resume Overview
   * Skill-Gap Coaching
   * Missing Keywords
   * Percentage Match
4. Review the AI-generated analysis.

## 📌 Notes

* Only the **first page** of the uploaded PDF is analyzed.
* Uploaded files are processed for the current session and are not permanently stored.
* Match scoring is designed to be **strict and realistic rather than overly generous**.
* A generic or poorly tailored resume may receive a lower score even when the candidate has relevant technical qualifications.

## 👨‍💻 Project Highlights

ResumeSense demonstrates practical experience with:

* Generative AI
* Gemini Vision
* Prompt Engineering
* PDF/Image Processing
* Streamlit Application Development
* ATS Optimization
* Job Description Analysis
* AI-powered Career Assistance


* **Live Demo:** (https://multi-perspective-ats-analyzer-ickf65gvqwvedteffqhghu.streamlit.app/)
