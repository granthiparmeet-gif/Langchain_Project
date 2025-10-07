from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

texts = [
    "FAISS enables efficient vector similarity search.",
    "IVF and PQ are indexing methods for scalable retrieval.",
    "LangChain integrates FAISS easily for RAG pipelines.",
    "HNSW uses graph structures for approximate nearest neighbor search.",
    "Vector databases help store embeddings for semantic search."
]

splitter = RecursiveCharacterTextSplitter(chunk_size= 100, chunk_overlap = 20)
docs = splitter.create_documents(texts)

embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

vector_store = FAISS.from_documents(docs, embeddings)

vector_store.save_local("faiss_index")

db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

query = "How does FAISS speed up vector search?"
results = db. similarity_search(query, k=3)


for i, res in enumerate(results):
    print(f"{i+1}.", res.page_content)
