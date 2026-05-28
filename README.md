# DPDP Privacy Assistant

An AI-powered multilingual privacy assistant built around India's Digital Personal Data Protection (DPDP) Act and related governance documents.

The assistant uses Retrieval-Augmented Generation (RAG) to answer user queries strictly from uploaded DPDP-related PDFs including:

* DPDP Act
* DPDP Rules
* AI Governance Guidelines
* Advisory documents

It supports:

* English and Hindi queries
* Semantic document retrieval
* Context-grounded AI responses
* Privacy-focused architecture
* No authentication
* No chat storage

---

# Features

* Multilingual support (English + Hindi)
* PDF ingestion pipeline
* Vector-based semantic search using ChromaDB
* Gemini-powered contextual responses
* FastAPI backend
* Modern chat-style web interface
* Markdown-rendered responses
* Source-aware answers
* Privacy-focused design

---

# Tech Stack

## Backend

* FastAPI
* Python
* ChromaDB
* Sentence Transformers
* Gemini API

## Frontend

* HTML
* CSS
* JavaScript

## AI / NLP

* RAG (Retrieval-Augmented Generation)
* `paraphrase-multilingual-MiniLM-L12-v2`
* Gemini Flash Models

---

# Project Structure

```text
dpdp-chatbot/
│
├── app/
│   ├── chatbot.py
│   ├── ingest.py
│   └── main.py
│
├── documents/
│   ├── act/
│   ├── rules/
│   └── advisories/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── vectorstore/
├── requirements.txt
└── .env
```

---

# How It Works

```text
PDF Documents
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
ChromaDB Vector Storage
      ↓
Semantic Retrieval
      ↓
Gemini Response Generation
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd dpdp-chatbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Get Gemini API key from:

https://aistudio.google.com/

---

# Add PDF Documents

Place DPDP-related PDFs inside:

```text
documents/
```

Example:

```text
documents/
├── act/
│   └── DPDP_Act.pdf
│
├── rules/
│   ├── DPDP_Rules_2025.pdf
│   └── AI_Guidelines.pdf
```

---

# Ingest Documents

Run:

```bash
python app/ingest.py
```

This:

* extracts text from PDFs
* creates embeddings
* stores vectors in ChromaDB

---

# Run The Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

# Example Queries

* What is consent under DPDP Act?
* डेटा प्रिंसिपल क्या होता है?
* Explain consent manager.
* Is there any AI governance guideline?
* What are obligations of Data Fiduciary?

---

# Privacy Design

This project is intentionally designed to:

* avoid storing user chats
* avoid authentication requirements
* minimize data retention
* focus only on DPDP-related guidance

---

# Future Improvements

* OCR for scanned Hindi PDFs
* Page-level citations
* Streaming responses
* Better legal source attribution
* Query filtering
* Deployment optimizations
* Mobile responsiveness
* Voice support

---

# Deployment

Recommended deployment architecture:

| Component    | Platform        |
| ------------ | --------------- |
| Frontend     | Vercel          |
| Backend      | Render          |
| Vector Store | Persistent Disk |

---

# Disclaimer

This assistant provides informational assistance only and should not be considered legal advice.

Always refer to official government notifications, legal professionals, or authoritative sources for legal interpretation.

---

# Author

© 2026 utkarshpandey.com
