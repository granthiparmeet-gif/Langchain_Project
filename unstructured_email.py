# from langchain_community.document_loaders import UnstructuredEmailLoader

# loader = UnstructuredEmailLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/sample_email.eml")
# docs = loader.load()

# print(f"Loaded {len(docs)} email(s)\n")
# for i, d in enumerate(docs, 1):
#     print(f"--- EMAIL {i} ---")
#     print("CONTENT:", d.page_content[:200])
#     print("METADATA:", d.metadata)


from langchain_community.document_loaders import UnstructuredEmailLoader

loader = UnstructuredEmailLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/sample_email.eml")
docs = loader.lazy_load()

for i, d in enumerate(docs, 1):
    print(f"--- EMAIL {i} ---")
    print("CONTENT:", d.page_content[:200])
    print("METADATA:", d.metadata)

