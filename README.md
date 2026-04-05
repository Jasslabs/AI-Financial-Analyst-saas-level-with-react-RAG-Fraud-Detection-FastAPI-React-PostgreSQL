# AI-Financial-Analyst-saas-level-with-react-RAG-Fraud-Detection-FastAPI-React-PostgreSQL
Upload a financial PDF Ask a question like: “What was the revenue growth last quarter?” Show source chunks used in the answer Enter a transaction amount and get fraud risk Show dashboard charts for transaction patterns
ai-financial-analyst/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── services/
│   │   ├── rag/
│   │   ├── db/
│   │   └── models/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
├── .env.example
└── demo/
    └── demo_script.md

    # 🚀 AI Financial Analyst

An end-to-end AI-powered financial analysis platform combining:
- 📊 Machine Learning (Fraud Detection)
- 🤖 LLM + RAG (Financial Q&A)
- 📄 PDF Processing (PyMuPDF)
- ⚡ FastAPI Backend
- 🧠 Vector Search (FAISS)
- 🗄 PostgreSQL Database
- 🌐 React Dashboard
- ☁️ Docker + AWS Deployment

---

## 🎯 Features

### 🔍 Financial Document Intelligence (RAG)
- Upload financial reports (PDFs)
- Ask questions like:
  - "What is the revenue growth?"
  - "Summarize key risks"
- Uses embeddings + vector search

### 💳 Fraud Detection System
- Detect suspicious transactions
- ML model: Isolation Forest
- Returns fraud score + classification

### 📊 Backend APIs (FastAPI)
- `/upload-pdf`
- `/ask`
- `/fraud`

---

## 🧠 Architecture

- Data → Processing (Pandas)
- ML → Fraud Detection
- RAG → LLM + FAISS
- API → FastAPI
- DB → PostgreSQL
- UI → React

---

## ⚙️ Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/yourusername/ai-financial-analyst.git
cd ai-financial-analyst
