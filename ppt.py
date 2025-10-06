from langchain_unstructured import UnstructuredLoader

loader = UnstructuredLoader("sample1.pptx")

docs = loader.load()

print("Total Slides:", len(docs))
for i, d in enumerate(docs[:2], 1):
    print(f"--- SLIDE {i} ---")
    print("CONTENT:", d.page_content[:250])
    print("METADATA:", d.metadata)
