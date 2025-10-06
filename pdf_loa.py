from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("/Users/parmeetsingh/Desktop/Langchain- Projects/Parmeet_Singh_Resume.pdf")

docs = loader.load()

print("Total Pages: ", len(docs),"\n")

for i,d in enumerate(docs,1):
    print(f"PAGE: {i}\n")
    print("PAGE CONTENT: \n ", d.page_content[:300])
    print("METADATA: \n", d.metadata)




