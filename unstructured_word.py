# from langchain_community.document_loaders import CSVLoader

# # Path to your CSV file
# loader = CSVLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/sample.csv")

# # Load the data
# docs = loader.load()

# # Peek into the first few rows as LangChain Documents
# for i, d in enumerate(docs[:3], 1):
#     print(f"--- ROW {i} ---")
#     print("CONTENT:", d.page_content)
#     print("METADATA:", d.metadata)


# from langchain_community.document_loaders import UnstructuredMarkdownLoader

# loader = UnstructuredMarkdownLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/sample.md")

# docs = loader.load()

# for i,d in enumerate(docs,1):
#     print(d.page_content, docs[0])
#     print(d.metadata)


from langchain_community.document_loaders import UnstructuredExcelLoader

loader = UnstructuredExcelLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/file_example_XLS_10.xls")

docs = loader.load()

print(f"Total Sheets (docs): {len(docs)}\n")

for i, d in enumerate(docs, 1):
    print(f"--- SHEET {i} ---")
    print("CONTENT:", d.page_content[:200])
    print("METADATA:", d.metadata)
    print()
