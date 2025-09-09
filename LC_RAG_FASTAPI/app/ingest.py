import os
from .utils import load_documents, split_documents
from .settings import get_settings
from .vectorstore import build_vectorstore

def main():
    s = get_settings()
    data_dir = os.path.abspath("data")
    print(f"[INGEST] Loading from {data_dir}")
    docs = load_documents(data_dir)
    print(f"[INGEST] Loaded {len(docs)} raw docs")
    chunks = split_documents(docs, s.CHUNK_SIZE, s.CHUNK_OVERLAP)
    print(f"[INGEST] Split into {len(chunks)} chunks")
    build_vectorstore(chunks)
    print("[INGEST] FAISS index saved to ./.faiss")

if __name__ == "__main__":
    main()