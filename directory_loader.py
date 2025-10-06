from langchain_community.document_loaders import DirectoryLoader, ImageCaptionLoader, TextLoader, PyMuPDFLoader

loader= [
    DirectoryLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/", glob= "*.jpeg",loader_cls=ImageCaptionLoader),
    DirectoryLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/", glob= "*.txt", loader_cls=TextLoader),
    DirectoryLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/", glob= "*.pdf", loader_cls=PyMuPDFLoader)
]

docs = []

for x in loader:
    docs.extend(x.load())

print(f"Loaded {len(docs)} multimodal documents")

# Quick preview
for i, d in enumerate(docs[:3], 1):
    print(f"\n--- DOC {i} ---")
    print(d.page_content[:200])
    print("Metadata:", d.metadata)

