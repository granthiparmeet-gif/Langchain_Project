from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


load_dotenv()

docs = [
    Document(page_content="Weaviate supports hybrid semantic and keyword search."),
    Document(page_content="pgVector is used for structured + unstructured data."),
    Document(page_content="FAISS is an open-source vector library."),
]

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding=embeddings)
base_retriever = vectorstore.as_retriever(search_type = "similarity", search_kwargs={"k":3})

llm =ChatOpenAI()
multi_retriever = MultiQueryRetriever.from_llm(llm=llm, retriever=base_retriever)
print("\nMULTIQUERY RESULTS:")
for d in multi_retriever.invoke("Explain Weaviate and pgVector"):
    print("-", d.page_content)

compressor = LLMChainExtractor.from_llm(llm)
compressed = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base_retriever)
print("\nCOMPRESSED RESULTS:")
for d in compressed.invoke("Summarize Weaviate use cases"):
    print("-", d.page_content)




