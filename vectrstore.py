from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"



load_dotenv()


docs = [
    Document(page_content="Weaviate is a vector database for hybrid search."),
    Document(page_content="pgVector adds vector search to PostgreSQL."),
    Document(page_content="Pinecone is a managed vector database."),
    Document(page_content="LangChain provides retrievers and chains for RAG.")
]

embeddings = OpenAIEmbeddings()

vector_store = FAISS.from_documents(docs, embeddings)

retriever_sim = vector_store.as_retriever(search_type="similarity", search_kwargs={"k":2})
retriver_mmr = vector_store.as_retriever(search_type = "mmr", search_kwags = {"k":2, "lambda_mult":0.5})



print ("SIMILARITY---")

for d in retriever_sim.invoke("What is a vector Database?"):
    print(d.page_content)

print("MMR")
for d in retriver_mmr.invoke("What is a vector Database"):
    print(d.page_content)