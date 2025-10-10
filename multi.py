from dotenv import load_dotenv
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.documents import Document

load_dotenv()

docs = [
    Document(page_content="Weaviate is a vector DB with hybrid search."),
    Document(page_content="Pinecone is a managed vector database."),
    Document(page_content="pgvector enables vector search in Postgres."),
    Document(page_content="FAISS is an in-memory vector index."),
]

embedding = OpenAIEmbeddings()
vector_store = Chroma.from_documents(docs, embedding=embedding)

simple_retriever = vector_store.as_retriever(search_type = "mmr", search_kwargs = {"k":3})

llm = ChatOpenAI()

multi = MultiQueryRetriever.from_llm(retriever=simple_retriever, llm=llm)

for d in multi.invoke("What are different vector databases?"):
    print(d.page_content)
