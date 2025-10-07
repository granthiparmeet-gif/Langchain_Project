import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()


texts = [
    "LangChain is a framework for building applications with LLMs.",
    "Vector embeddings help represent text as numbers for similarity search.",
    "FAISS is a library for efficient similarity search."
]

docs = [Document(page_content=t) for t in texts]

# embeddings  = OpenAIEmbeddings(model="text-embedding-3-large")

embeddings = HuggingFaceEmbeddings(model_name="bge-base-en-v1.5")

db = FAISS.from_documents(docs,embeddings, distance_strategy="COSINE")

results = db.similarity_search("How to find similar meanings using AI?", k=2)

for i,d in enumerate(results,1):
    print(i,":", d.page_content)
