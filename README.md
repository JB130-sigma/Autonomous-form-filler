# Multilingual Agentic Document Processor

An AI-powered multilingual document processing system that automatically extracts, validates, and processes information from documents. The system uses OCR, AI agents, Retrieval-Augmented Generation (RAG), and browser automation to intelligently fill online forms with minimal human intervention.

---

## 📖 Project Overview

Many government, educational, banking, and enterprise workflows require users to manually enter information from documents into online forms. This process is repetitive, time-consuming, and prone to human error.

The **Multilingual Agentic Document Processor** automates this workflow by:

- Extracting text from multilingual documents
- Understanding document structure using AI
- Validating extracted information
- Retrieving missing details through RAG
- Automatically filling web forms using browser automation

---

## 🎯 Objectives

- Automate document processing
- Support multilingual documents
- Reduce manual data entry
- Improve extraction accuracy
- Enable intelligent decision-making using AI agents
- Automatically fill online forms

---

## ✨ Features

### ✅ Authentication
- User Registration
- User Login
- JWT Authentication
- Password Hashing (bcrypt)

### 🚧 Document Processing
- PDF Upload
- Image Upload
- OCR using PaddleOCR
- Layout Detection
- Table Extraction
- Handwritten Text Support (Planned)

### 🚧 AI Processing
- Document Classification
- Intelligent Information Extraction
- Field Validation
- Confidence Scoring
- Missing Data Detection

### 🚧 RAG
- Semantic Search
- Context Retrieval
- Vector Database (FAISS)
- Sentence Transformers

### 🚧 Agentic Workflow
- LangGraph Agent Pipeline
- Multi-Agent Decision Making
- Document Verification
- Validation Agent
- Correction Agent

### 🚧 Browser Automation
- Automatic Form Filling
- Playwright Integration
- Multi-Step Form Support
- Error Handling

---

## 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- Pydantic

### AI & Machine Learning
- LangChain
- LangGraph
- PaddleOCR
- LayoutParser
- Sentence Transformers
- FAISS

### Image Processing
- OpenCV
- Pillow
- NumPy

### Automation
- Playwright

### Utilities
- Loguru
- RapidFuzz
- HTTPX

---

## 📂 Project Structure

```text
Multilingual-Agentic-Document-Processor/
│
├── backend/
│   ├── app/
│   ├── uploads/
│   ├── data/
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
├── docs/
├── docker/
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/Multilingual-Agentic-Document-Processor.git
```

### Navigate

```bash
cd Multilingual-Agentic-Document-Processor/backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Copy

```text
.env.example
```

to

```text
.env
```

and configure the required environment variables.

### Run Backend

```bash
uvicorn app.main:app --reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📅 Development Roadmap

- ✅ Project Setup
- ✅ Authentication Module
- ⏳Document Upload
- ⏳ OCR Integration
- ⏳ Layout Detection
- ⏳ Document Parsing
- ⏳ RAG Pipeline
- ⏳ Validation Engine
- ⏳ LangGraph Workflow
- ⏳ Playwright Form Filling
- ⏳ Frontend Dashboard
- ⏳ Docker Deployment

---

## 📌 Current Status

**Version:** 1.0.0

Completed:
- Project architecture
- Database setup
- Authentication system
- JWT security
- API documentation

Currently Working On:
- Document Upload Module

---

## 👨‍💻 Contributors

- Jeet Bhandari

---

## 📄 License

This project is developed for academic and research purposes as a Final Year Engineering Project.
