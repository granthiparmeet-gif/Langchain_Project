# import os
# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# from dotenv import load_dotenv
# from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings
# from langchain_core.documents import Document
# from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
# from langchain.retrievers.contextual_compression import ContextualCompressionRetriever

# load_dotenv()

# docs = [
#     Document(page_content="Weaviate provides hybrid search using BM25 and vector embeddings."),
#     Document(page_content="FAISS is a library for similarity search in high-dimensional vectors."),
#     Document(page_content="BM25 is a lexical retrieval algorithm using term frequency and IDF."),
# ]

# emb = OpenAIEmbeddings()
# v_store = Chroma.from_documents(docs, embedding=emb)
# retriever = v_store.as_retriever(search_kwargs={"k": 5})


# reranker = FlashrankRerank(top_n=3)

# rerank_retriever = ContextualCompressionRetriever(
#     base_retriever=retriever,
#     base_compressor=reranker,
# )

# results = rerank_retriever.invoke("hybrid search")

# for i, doc in enumerate(results):
#     print(f"Rank {i+1}:", doc.page_content)

# crossencoder_rerank.py
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # macOS OpenMP quirk

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# ✅ Cross-encoder pieces (updated imports)
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers.document_compressors.cross_encoder_rerank import CrossEncoderReranker
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever

load_dotenv()  # expects OPENAI_API_KEY if you use OpenAIEmbeddings

# 1) Tiny corpus
docs = [
    Document(page_content="Weaviate provides hybrid search using BM25 and vector embeddings."),
    Document(page_content="FAISS is a library for efficient similarity search in vector spaces."),
    Document(page_content="BM25 is a lexical retrieval algorithm based on term frequency and IDF."),
    Document(page_content="LangChain supports rerankers like CrossEncoder and Cohere."),
]

# 2) Vector store + base retriever
emb = OpenAIEmbeddings()
vstore = Chroma.from_documents(docs, embedding=emb)
base_retriever = vstore.as_retriever(search_kwargs={"k": 4})

# 3) Build a HuggingFace cross-encoder model INSTANCE (required)
cross_encoder_model = HuggingFaceCrossEncoder(
    model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"
)

# 4) Wrap model with the CrossEncoderReranker (the actual compressor/reranker)
reranker = CrossEncoderReranker(model=cross_encoder_model, top_n=3)

# 5) Compose: retrieval → rerank
hybrid_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=reranker,   # NOTE: pass the reranker, not the model
)

# 6) Query
query = "What is hybrid search in vector databases?"
results = hybrid_retriever.invoke(query)

print("\nReranked results:")
for i, d in enumerate(results, 1):
    print(f"{i}. {d.page_content}")
    # If you want to peek at metadata to see scores, uncomment:
    # print("   meta:", d.metadata)


