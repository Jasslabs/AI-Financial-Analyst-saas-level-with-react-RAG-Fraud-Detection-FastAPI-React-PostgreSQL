# backend/app/main.py
from fastapi import FastAPI, UploadFile, File
from app.services.pdf_ingestion import extract_text_from_pdf, chunk_text
from app.rag.embeddings import add_documents
from app.rag.chain import answer_question
from app.services.fraud import predict_fraud

app = FastAPI()

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)
    add_documents(chunks)

    return {"message": "PDF processed successfully", "chunks": len(chunks)}

@app.get("/ask")
def ask(question: str):
    return {"answer": answer_question(question)}

@app.get("/fraud")
def fraud(amount: float):
    return predict_fraud(amount)