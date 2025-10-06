# from langchain_unstructured import UnstructuredLoader

# loader = UnstructuredLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/basic.txt")

# docs = loader.load()

# for i,d in enumerate(docs,1):
#     print("PAGE", i)
#     print("CONTENT:", d.page_content[:200])
#     print("METADATA:" , d.metadata)


# from langchain_unstructured import UnstructuredLoader

# loader = UnstructuredLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/resume.docx")

# docs = loader.load()

# print("Extracted Text", docs[0].page_content[:300])

# from langchain_unstructured import UnstructuredLoader

# loader = UnstructuredLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/langchain.html")

# docs = loader.load()

# for d in docs:
#     print("Preview", d.page_content[:600])
#     print("Metadata", d.metadata)


from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/sample1.docx")
docs = loader.load()

for i, d in enumerate(docs, 1):
    print("DOCX PART", i)
    print("CONTENT:", d.page_content[:200])
    print("METADATA:", d.metadata)
