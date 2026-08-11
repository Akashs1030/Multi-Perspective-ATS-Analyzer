from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-3.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------
# Custom CSS (UI only — no logic below this block is changed)
# ------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: radial-gradient(circle at 10% 10%, #1b1f3b 0%, #0d0f1f 45%, #05060d 100%);
    color: #eef0ff;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #12142b 0%, #0a0b18 100%);
    border-right: 1px solid rgba(255,255,255,0.06);
}
section[data-testid="stSidebar"] * {
    color: #d8daf5 !important;
}

.ats-hero {
    padding: 2.2rem 2rem;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(99,102,241,0.18), rgba(236,72,153,0.12));
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 1.6rem;
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
}
.ats-hero h1 {
    font-family: 'Poppins', sans-serif;
    font-size: 2.1rem;
    font-weight: 700;
    margin: 0 0 0.35rem 0;
    background: linear-gradient(90deg, #a5b4fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.ats-hero p {
    color: #b8bce0;
    font-size: 0.98rem;
    margin: 0;
}

.stTextArea label, .stFileUploader label {
    font-family: 'Poppins', sans-serif;
    font-weight: 600 !important;
    font-size: 1rem !important;
    color: #e6e8ff !important;
}

.stTextArea textarea {
    background-color: #12142b !important;
    color: #eef0ff !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
}

[data-testid="stFileUploaderDropzone"] {
    background-color: #12142b !important;
    border: 1.5px dashed rgba(165,180,252,0.45) !important;
    border-radius: 14px !important;
}

.stButton > button {
    width: 100%;
    padding: 0.75rem 1rem;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.10);
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: white;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
    letter-spacing: 0.2px;
    transition: transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
    box-shadow: 0 4px 14px rgba(79,70,229,0.35);
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(124,58,237,0.45);
    opacity: 0.96;
}
.stButton > button:active {
    transform: translateY(0px);
}

.ats-result-card {
    background: #12142b;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin-top: 1rem;
    box-shadow: 0 6px 24px rgba(0,0,0,0.3);
    animation: fadeIn 0.4s ease;
}
.ats-result-card h3 {
    font-family: 'Poppins', sans-serif;
    color: #a5b4fc;
    margin-top: 0;
    font-size: 1.15rem;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

.stAlert {
    border-radius: 12px !important;
}

hr {
    border-color: rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 📄 ATS Resume Expert")
    st.markdown(
        "Upload a resume and a job description, then pick an analysis "
        "mode below. Powered by Gemini."
    )
    st.markdown("---")
    st.markdown("**How it works**")
    st.markdown(
        "1. Paste the job description\n"
        "2. Upload your resume (PDF)\n"
        "3. Choose an analysis action\n"
        "4. Review the AI-generated report"
    )
    st.markdown("---")
    st.caption("Your files are processed only for this session.")

# ------------------------------------------------------------------
# Hero header
# ------------------------------------------------------------------
st.markdown("""
<div class="ats-hero">
    <h1>ATS Tracking System</h1>
    <p>Analyze your resume against any job description — get recruiter-style feedback, skill-gap coaching, missing keywords, and a match score.</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Inputs
# ------------------------------------------------------------------
col1, col2 = st.columns([1.3, 1], gap="large")

with col1:
    input_text = st.text_area("Job Description: ", key="input", height=220,
                               placeholder="Paste the job description here...")

with col2:
    uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])
    if uploaded_file is not None:
        st.success("PDF Uploaded Successfully")

st.markdown("---")
st.markdown("#### Choose an analysis")

b1, b2, b3, b4 = st.columns(4)
with b1:
    submit1 = st.button("🧑‍💼 Tell Me About the Resume")
with b2:
    submit2 = st.button("📈 How Can I Improvise my Skills")
with b3:
    submit3 = st.button("🔍 What are the Keywords That are Missing")
with b4:
    submit4 = st.button("🎯 Percentage match")

input_prompt1 = """
You are an expert technical recruiter and resume reviewer with over 15 years of experience screening 
candidates for tech roles. Analyze the  resume, Give a concise, structured overview covering 
who the candidate is and their experience level in 2-3 sentences, followed by their 3-4 key strengths 
starting with the most impressive, then 2-3 notable projects or achievements with quantifiable impact 
where present, and finally a brief overall impression of how the resume reads to a recruiter. Reference 
specific details from the resume rather than generic statements, do not invent information that isn't
 present in the text,
"""



input_prompt2 = """
You are a career coach and technical mentor who specializes in helping candidates close skill gaps for competitive tech roles. 
Given resume and, if available, the target job description, identify where the candidate can grow.
 Point out 3-4 skills that are already present but underdeveloped and explain why they matter, then suggest 2-3 skills that are missing but 
 valuable for this candidate's career trajectory, and for every skill mentioned give one concrete, actionable next step such as a specific project,
  certification, or practice method rather than vague advice. Tie every suggestion directly to evidence from the resume, avoid generic phrases like
 "improve communication skills,"
"""



input_prompt3="""
You are an ATS optimization specialist with deep expertise in resume parsing algorithms and recruiter keyword matching. Compare the resume against
 the job description and identify the keywords critical for ATS scoring that are missing. List the missing hard skills, tools,
  and technical terms that appear in the job description but are absent or underrepresented in the resume, then list any missing soft-skill or 
  role-related keywords such as "cross-functional" or "stakeholder management" if relevant, and suggest which section of the resume each keyword 
should naturally be added to without encouraging keyword stuffing. Only flag keywords that are genuinely relevant and truthfully applicable, never
 suggest fabricating experience, and if the resume already covers a concept using different wording, note it as a synonym match rather than a
  missing keyword.
"""


input_prompt4 = """
You are an ATS scoring engine that calculates a resume-to-job-description match percentage using a weighted evaluation of skills, 
experience, and keyword overlap, where technical skills account for 40%, experience relevance accounts for 20%, keyword overlap accounts 
for 25%, and domain relevance accounts for 15%. Using this resume and the job description, calculate an 
overall match percentage and give a one-line reason for each of the four sub-scores, followed by a short, honest one-to-two sentence verdict 
on whether the candidate should apply. Be strict and realistic rather than generous, 
and make sure a generic, untailored resume scores low even if the candidate is technically qualified.
"""


def render_result(response_text):
    st.markdown('<div class="ats-result-card"><h3>📋 The Response is</h3></div>', unsafe_allow_html=True)
    st.write(response_text)


if submit1:
    if uploaded_file is not None:
        with st.spinner("Analyzing resume..."):
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt1,pdf_content,input_text)
        render_result(response)
    else:
        st.warning("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        with st.spinner("Identifying skill gaps..."):
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt2,pdf_content,input_text)
        render_result(response)
    else:
        st.warning("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        with st.spinner("Scanning for missing keywords..."):
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt3,pdf_content,input_text)
        render_result(response)
    else:
        st.warning("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        with st.spinner("Calculating match percentage..."):
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt4,pdf_content,input_text)
        render_result(response)
    else:
        st.warning("Please upload the resume")