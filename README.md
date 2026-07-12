# Agentic Form Filling System

An AI-powered backend system that automatically understands application forms, identifies the required supporting documents, extracts information from uploaded documents, validates user data, and intelligently fills application forms.

The project follows a modular **Agentic AI Architecture**, where specialized AI agents collaborate to automate the complete document processing and form filling workflow.

---

# ✨ Features

- 🔐 JWT Authentication
- 📁 Application Management
- 📤 Upload Images & PDF Documents
- 🤖 AI Document Classification
- 🪪 Identity Document Detection
- 📄 Blank Form Detection
- 📝 OCR Extraction
- 📚 PDF OCR Support
- 🗂 Required Document Identification
- 🔄 Modular AI Agent Architecture
- 🌐 Multilingual Ready
- ⚡ OpenRouter LLM Integration

---

# 🏗 Architecture

```
USER
                      │
                      ▼
              Login/Register
                      │
                      ▼
           Create Application
                      │
                      ▼
          Upload Any Document
                      │
                      ▼
      🤖 Document Classification Agent
                      │
      ┌───────────────┴───────────────┐
      │                               │
      ▼                               ▼
Blank Form                     Identity Document
      │                               │
      ▼                               ▼
🤖 Form Analyzer Agent          Store Document
      │
      ▼
Required Fields
      │
      ▼
🤖 Document Requirement Agent
      │
      ▼
Ask User for Missing Documents
      │
      ▼
User Uploads Remaining Documents
      │
      ▼
🤖 OCR + Parser Agent
      │
      ▼
🤖 Validation Agent
      │
      ▼
🤖 Form Filling Agent
      │
      ▼
Download / Submit
```

---

# 🤖 AI Agents

## 1. Document Classification Agent

Analyzes uploaded documents using a Vision LLM.

Responsibilities:

- Detect document type
- Detect blank forms
- Identify identity documents
- Categorize uploaded files
- Estimate confidence
- Identify required supporting documents

Supported Documents:

- Aadhaar Card
- PAN Card
- Passport
- Driving Licence
- Voter ID
- Passport Application Form
- Bank Account Opening Form
- College Admission Form
- Scholarship Form
- Utility Bill
- Bank Statement
- Passport Photo
- Signature
- Blank Forms

---

## 2. Form Analyzer Agent

Analyzes uploaded application forms.

Responsibilities:

- Detect form name
- Understand document layout
- Identify all input fields
- Detect required fields
- Determine field types
- Prepare the form for intelligent filling

---

## 3. Document Requirement Agent

Determines which supporting documents are required for a particular application form.

Example:

Passport Application →

- Aadhaar
- Passport Photo
- Signature

Bank Account Opening →

- Aadhaar
- PAN
- Passport Photo
- Signature

---

## 4. OCR + Parser Agent

Extracts and structures information from uploaded documents.

Current OCR Engine:

- EasyOCR

Future Support:

- Gemini Vision OCR
- Hybrid OCR Pipeline

Responsibilities:

- Extract printed text
- OCR for PDF documents
- OCR for Images
- Parse extracted information into structured data

---

## 5. Validation Agent

Validates extracted information before form filling.

Responsibilities:

- Required field validation
- Missing document detection
- Invalid field detection
- Duplicate document checking
- Confidence verification

---

## 6. Form Filling Agent

Automatically fills application forms using validated information.

Responsibilities:

- Map extracted values
- Auto-fill application forms
- Preserve original formatting
- Generate completed forms

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication

## AI & LLM

- OpenRouter
- Google Gemini 2.5 Flash
- Agentic AI Workflow

## OCR

- EasyOCR
- PyMuPDF

## Database

- SQLite (Development)
- PostgreSQL (Production Ready)

## Storage

- Local File Storage

---

# 📂 Project Structure

```
backend/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── enums/
│   ├── llm/
│   ├── models/
│   ├── ocr/
│   ├── prompts/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── uploads/
│   └── main.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Multilingual-Agentic-Form-Filler.git
```

Navigate to the backend

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙ Environment Variables

Create a `.env` file

```env
PROJECT_NAME=Multilingual Agentic Form Filling System

OPENROUTER_API_KEY=your_api_key

OPENROUTER_MODEL=google/gemini-2.5-flash

DATABASE_URL=sqlite:///./app.db

SECRET_KEY=your_secret_key
```

---

# ▶ Running the Server

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📌 Current Capabilities

- User Authentication
- Application Creation
- Image Upload
- PDF Upload
- Document Storage
- AI Document Classification
- Blank Form Detection
- Identity Document Detection
- OCR Text Extraction
- PDF OCR Processing
- Required Document Identification
- Modular Agent-Based Backend

---

# 🔮 Future Enhancements

- Gemini Vision OCR
- Intelligent Form Understanding
- Information Extraction Agent
- Multi-language OCR
- Automatic Form Filling
- Filled PDF Generation
- Digital Signature Support
- Cloud Storage Integration
- Human-in-the-loop Review
- Frontend Dashboard
- Deployment on Cloud

---

# 🎯 Vision

To build an intelligent multilingual AI platform capable of understanding documents, identifying required information, validating user data, and automatically completing government, banking, educational, and enterprise application forms using a collaborative multi-agent AI architecture.

---

# 📄 License

This project is developed for educational and research purposes.
