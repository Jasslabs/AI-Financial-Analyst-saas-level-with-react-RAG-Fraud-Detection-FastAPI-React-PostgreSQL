# backend/app/rag/chain.py
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from app.rag.embeddings import search

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate.from_template("""
You are a finance assistant.
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer in a clear, professional way.
""")

def answer_question(question: str):
    context_docs = search(question)
    context = "\n".join(context_docs)

    formatted_prompt = prompt.format(context=context, question=question)
    response = llm.invoke(formatted_prompt)
    return response.content