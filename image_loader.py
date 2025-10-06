from langchain_community.document_loaders import UnstructuredImageLoader

docs = UnstructuredImageLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/download.jpeg").load()


print(docs[0].page_content)
