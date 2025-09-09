from fastapi import FastAPI, HTTPException
from typing import List
from .schemas import ChatRequest, ChatResponse
from .settings import get_settings
from .utils import format_docs
from .vectorstore import get_vectorstore
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

app = FastAPI(title="LangChain RAG FastAPI Starter", version="1.0.0")

SYSTEM_PROMPT = (
    "You are a concise, helpful assistant. Use the provided context to answer the user.\n"
    "If the answer isn't in the context, say you don't know. Always cite sources as [n]."
)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "Question: {question}\n\nContext:\n{context}")
])

def make_rag_chain():
    s = get_settings()
    llm = ChatOpenAI(model=s.CHAT_MODEL, temperature=0, api_key=s.OPENAI_API_KEY)
    retriever = get_vectorstore().as_retriever(search_kwargs={"k": s.K})
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain, retriever

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    rag_chain, retriever = make_rag_chain()
    # allow override of k
    if req.k:
        retriever.search_kwargs["k"] = req.k
    try:
        answer: str = rag_chain.invoke(req.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Fetch sources for transparency
    docs = retriever.get_relevant_documents(req.question)
    unique_sources: List[str] = []
    for d in docs:
        src = d.metadata.get("source", "unknown")
        if src not in unique_sources:
            unique_sources.append(src)

    return ChatResponse(answer=answer, sources=unique_sources)

@app.post("/reindex")
def reindex():
    # convenience alias; actual building is done via CLI in app.ingest
    try:
        import subprocess, sys
        r = subprocess.run([sys.executable, "-m", "app.ingest"], check=True, capture_output=True, text=True)
        return {"status": "ok", "log": r.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ingest")
def ingest():
    # same as /reindex but explicit
    return reindex()

# ----------------------
# Local CLI (optional)
# ----------------------
if __name__ == "__main__":
    chain, _ = make_rag_chain()
    print("RAG ready. Type questions; Ctrl+C to exit.\n")
    try:
        while True:
            q = input("You: ")
            if not q.strip():
                continue
            print("\nAssistant:", chain.invoke(q), "\n")
    except KeyboardInterrupt:
        print("\nBye!")