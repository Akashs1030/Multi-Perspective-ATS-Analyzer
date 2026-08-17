# ResumeSense – Multi-Perspective ATS Analyzer

ResumeSense is an AI-powered resume analysis tool that evaluates resumes against job descriptions using Google Gemini's vision capabilities. Instead of relying on error-prone text extraction, it converts resumes directly into image input for the LLM, preserving layout and formatting context during analysis.

## Features

- **Multi-mode analysis** — four distinct evaluation modes in a single app:
  - 🧑‍💼 **Tell Me About the Resume** — recruiter-style overview of candidate profile, strengths, and notable projects
  - 📈 **How Can I Improvise My Skills** — career-coach feedback identifying underdeveloped skills and actionable growth steps
  - 🔍 **What Are the Keywords That Are Missing** — ATS-optimization scan comparing resume against a job description for missing hard/soft skills
  - 🎯 **Percentage Match** — weighted JD-match score (skills 40%, experience 20%, keyword overlap 25%, domain relevance 15%)
- **Vision-based parsing** — resumes are converted to images and analyzed directly by Gemini, avoiding the formatting/parsing errors common with text-extraction-based ATS tools
- **Specialized prompt engineering** — each mode uses a purpose-built prompt template tuned to a specific evaluation behavior
- **Polished UI** — custom-styled Streamlit interface with sidebar guidance, gradient hero header, and animated result cards

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM:** Google Gemini (Vision) via `google-generativeai`
- **PDF Processing:** `pdf2image`, `Pillow (PIL)`
- **Environment Management:** `python-dotenv`

## How It Works

1. User pastes a job description and uploads a resume (PDF)
2. The first page of the resume is converted to a JPEG image and base64-encoded
3. User selects one of four analysis modes
4. The corresponding prompt + resume image are sent to Gemini
5. Gemini's response is rendered in a styled result card

## Setup

1. Clone the repository
   ```bash
   git clone <repo-url>
   cd resumesense
   ```

2. Install dependencies
   ```bash
   pip install streamlit google-generativeai pdf2image pillow python-dotenv
   ```

3. Install `poppler` (required by `pdf2image`)
   - **Windows:** download poppler binaries and add to PATH
   - **macOS:** `brew install poppler`
   - **Linux:** `sudo apt-get install poppler-utils`

4. Add your Gemini API key to a `.env` file
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. Run the app
   ```bash
   streamlit run app.py
   ```

## Usage

1. Paste the target job description into the text area
2. Upload your resume as a PDF
3. Choose an analysis mode:
   - Resume overview
   - Skill-gap coaching
   - Missing keywords
   - Percentage match
4. Review the AI-generated report

## Notes

- Only the first page of the uploaded PDF is analyzed
- Files are processed only for the current session and are not stored
- Match scoring is designed to be strict and realistic rather than generous — a generic, untailored resume should score low even for a technically qualified candidate

## License

MIT
