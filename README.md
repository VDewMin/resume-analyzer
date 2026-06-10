# 📄 AI Resume Analyzer

An AI-powered web application that analyzes your resume against a job description and provides instant feedback on your fit for the role.

## 🚀 Features

- Upload your resume as a PDF
- Paste any job description
- Get an AI-generated match score (0–100)
- See matched and missing skills at a glance
- Receive 3 specific strengths and improvement suggestions
- Get a rewritten professional summary tailored to the role

## 🛠️ Tech Stack

- **Python** — core language
- **Streamlit** — web interface
- **Google Gemini 2.5 Flash API** — AI analysis engine
- **pdfplumber** — PDF text extraction
- **python-dotenv** — environment variable management

## ⚙️ Setup & Installation

1. Clone the repository
```bash
   git clone https://github.com/VDewMin/resume-analyzer.git
   cd resume-analyzer
```

2. Create and activate a virtual environment
```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file and add your Gemini API key

5. Run the app
```bash
   streamlit run app.py
```

## 📸 Demo

Upload your resume PDF, paste a job description, and click Analyze.

## 🔑 Getting a Gemini API Key

Get a free API key at [aistudio.google.com](https://aistudio.google.com)