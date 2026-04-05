#Build embeddings and store in FAISS
# backend/app/rag/embeddings.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
stored_chunks = []

def add_documents(chunks):
    global stored_chunks
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings).astype("float32"))
    stored_chunks.extend(chunks)

def search(query, top_k=3):
    q_emb = model.encode([query]).astype("float32")
    distances, ids = index.search(q_emb, top_k)
    return [stored_chunks[i] for i in ids[0] if i != -1]