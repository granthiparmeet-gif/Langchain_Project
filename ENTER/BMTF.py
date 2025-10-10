from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from langchain_community.retrievers import TFIDFRetriever



docs = [
    Document(page_content="Weaviate is a vector database with hybrid search."),
    Document(page_content="pgvector adds vector search to PostgreSQL."),
    Document(page_content="BM25 is a lexical keyword ranking function."),
    Document(page_content="LangChain has retrievers for RAG pipelines."),
]


bm25 = BM25Retriever.from_documents(docs)
bm25.k = 2

for d in bm25.invoke("Lexical Ranking"):
    print(d.page_content)

tfid = TFIDFRetriever.from_documents(docs)
tfid.k = 3

for d in tfid.invoke("keyword method"):
    print(d.page_content)

    

