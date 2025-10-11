from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.documents import Document
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

load_dotenv()

docs = [
    Document(page_content="Weaviate supports hybrid search (BM25 + vectors) for semantic retrieval."),
    Document(page_content="pgvector adds ANN search over embeddings to PostgreSQL."),
    Document(page_content="This line is filler and should be pruned by compression."),
]

emb = OpenAIEmbeddings()

vector_store = Chroma.from_documents(docs, embedding=emb)
retriever = vector_store.as_retriever(search_type = "similarity", serach_kwargs = {"k":3})

llm = ChatOpenAI()
compressor = LLMChainExtractor.from_llm(llm)

cc=ContextualCompressionRetriever(base_compressor=compressor, base_retriever=retriever)

for d in cc.invoke("Explain hybrid search briefly"):
    print(d.page_content)