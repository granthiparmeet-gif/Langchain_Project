from langchain_community.document_loaders import TextLoader
from peek import peek

loader = TextLoader("data/notes.txt", encoding = "utf-8")

docs = loader.load()

peek(docs)