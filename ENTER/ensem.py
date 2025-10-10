from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers.ensemble import EnsembleRetriever


load_dotenv()

docs = [Document(page_content=t) for t in [
    "Weaviate hybrid search and schema filters.",
    "pgvector extends Postgres with vector search.",
    "BM25 is lexical keyword ranking.",
    "LangChain retrievers enable hybrid RAG pipelines."
]]

emb = OpenAIEmbeddings()
vstore = Chroma.from_documents(docs, embedding=emb)
semantic_retriever = vstore.as_retriever(search_type = "mmr", search_kwargs = {"k":3})

bm25 = BM25Retriever.from_documents(docs)
bm25.k = 3

ensemble = EnsembleRetriever(
    retrievers=[semantic_retriever, bm25],
    weights=[0.6,0.4]
)

results = ensemble.invoke("hybrid vector search")
for doc in results:
    print("-", doc.page_content)