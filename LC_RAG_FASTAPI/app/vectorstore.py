import os, pickle
from typing import Optional, Tuple, List
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from .settings import get_settings

_cache = {"vs": None}
_INDEX_DIR = ".faiss"

def _embedder():
    s = get_settings()
    return OpenAIEmbeddings(model=s.EMBED_MODEL, api_key=s.OPENAI_API_KEY)

def save_vectorstore(vs: FAISS):
    os.makedirs(_INDEX_DIR, exist_ok=True)
    vs.save_local(_INDEX_DIR)

def load_vectorstore() -> Optional[FAISS]:
    if not os.path.isdir(_INDEX_DIR):
        return None
    try:
        return FAISS.load_local(_INDEX_DIR, _embedder(), allow_dangerous_deserialization=True)
    except Exception as e:
        print(f"[WARN] Could not load FAISS index: {e}")
        return None

def get_vectorstore() -> FAISS:
    if _cache.get("vs") is not None:
        return _cache["vs"]
    vs = load_vectorstore()
    if vs is None:
        raise RuntimeError("Vectorstore not built. Run ingestion first (POST /ingest or python -m app.ingest).")
    _cache["vs"] = vs
    return vs

def build_vectorstore(chunks: List[Document]) -> FAISS:
    vs = FAISS.from_documents(chunks, _embedder())
    save_vectorstore(vs)
    _cache["vs"] = vs
    return vs