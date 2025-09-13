from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

loader = PyPDFLoader("sample.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

retriever = vectorstore.as_retriever()
llm = ChatOpenAI(model="gpt-3.5-turbo")
qa = RetrievalQA.from_chain_type(llm, retriever=retriever)

while True:
    query = input("Ask something about the PDF (or type 'exit'): ")
    if query.lower() == "exit":
        break
    answer = qa.run(query)
    print("Answer:", answer)
