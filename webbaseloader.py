from langchain_community.document_loaders import UnstructuredURLLoader

loader = UnstructuredURLLoader(["https://docs.langchain.com/docs/","https://python.langchain.com/docs/expression_language"])

docs = loader.load()

print("CONTENT PREVIEW:", docs[0].page_content[:300])
print("METADATA:", docs[0].metadata)