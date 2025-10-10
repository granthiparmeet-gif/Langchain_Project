from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

docs = [
    Document(page_content="Weaviate is a vector database with hybrid search."),
    Document(page_content="pgvector adds vector search to PostgreSQL."),
    Document(page_content="BM25 is a lexical keyword ranking function."),
    Document(page_content="LangChain has retrievers for RAG pipelines."),
]

embeddings = OpenAIEmbeddings()
vector_store = Chroma.from_documents(docs, embedding=embeddings)

query = "Vector Datbase"

print("MMR")
retriever = vector_store.as_retriever(search_type ="mmr", search_kwargs = {"k":3})
for d in retriever.invoke(query):
    print(d.page_content)

print("Similarity")
retriever = vector_store.as_retriever(search_type = "similarity", search_kwargs={"k":4})
for d in retriever.invoke(query):
    print(d.page_content)

