from fastapi import FastAPI
app = FastAPI(title="Financial RAG Chatbot")
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/api/v1/chat")
def chat(q: str): return {"answer": f"RAG answer for {q}", "sources":3}
