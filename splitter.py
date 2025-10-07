# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text = """ LangChain is a framework for developing applications powered by language models.
# It provides tools for connecting LLMs to external data sources, integrating them with APIs,
# and composing complex reasoning workflows."""

# splitter = RecursiveCharacterTextSplitter(chunk_size = 80, chunk_overlap = 20)

# chunks = splitter.split_text(text)

# for i,c in enumerate(chunks,1):
#     print(f"Chunk {i}:")
#     print(c)
#     print("---")



from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
LangChain is a framework for developing applications powered by language models.
# It provides tools for connecting LLMs to external data sources, integrating them with APIs,
# and composing complex reasoning workflows.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=80, 
    chunk_overlap = 20,
    separators=["\n\n","\n"," ","",]
    )

chunk = splitter.split_text(text)


for i,c in enumerate(chunk,1):
    print(f"Chunk no. : {i}")
    print(c)
    print("--"*50)