from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings , ChatOpenAI
from langchain_core.documents import Document
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers.self_query.chroma import ChromaTranslator
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(page_content="Weaviate hybrid search intro", metadata={"source": "blog", "year": 2023}),
    Document(page_content="pgvector quickstart guide", metadata={"source": "docs", "year": 2024}),
    Document(page_content="BM25 vs semantic retrieval", metadata={"source": "blog", "year": 2022}),
]

emb = OpenAIEmbeddings()
v_store = Chroma.from_documents(docs, embedding=emb)

metadata_field_info = [
    AttributeInfo(name="source", description="Where it comes from ", type="string"),
    AttributeInfo(name="year", description="Which year", type="integer")
]

document_content_description = "Technical Tutorials about serach algorithms"

llm = ChatOpenAI()

retriever = SelfQueryRetriever.from_llm(
    llm = llm,
    vectorstore=v_store,
    document_contents=document_content_description,
    metadata_field_info=metadata_field_info,
    structured_query_translator=ChromaTranslator(),
    search_kwargs = {"k":2}
)

results = retriever.invoke("Find docs after 2023 from official documentation")
for doc in results:
    print("-", doc.page_content, doc.metadata)