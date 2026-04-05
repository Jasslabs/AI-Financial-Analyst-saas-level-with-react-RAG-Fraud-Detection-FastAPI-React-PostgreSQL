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
