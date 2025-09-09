from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os

def load_documents(data_dir: str) -> List[Document]:
    docs: List[Document] = []
    for root, _, files in os.walk(data_dir):
        for f in files:
            path = os.path.join(root, f)
            ext = os.path.splitext(f)[1].lower()
            try:
                if ext == ".pdf":
                    loader = PyPDFLoader(path)
                    docs.extend(loader.load())
                elif ext in (".md", ".txt"):
                    loader = TextLoader(path, autodetect_encoding=True)
                    docs.extend(loader.load())
            except Exception as e:
                print(f"[WARN] Failed to load {path}: {e}")
    return docs

def split_documents(docs: List[Document], chunk_size: int, chunk_overlap: int) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def format_docs(docs: List[Document]) -> str:
    parts = []
    for i, d in enumerate(docs, start=1):
        src = d.metadata.get("source", "unknown")
        parts.append(f"[{i}] {src}:\n{d.page_content}")
    return "\n\n".join(parts)