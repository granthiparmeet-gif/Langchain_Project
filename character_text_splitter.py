from langchain_text_splitters import CharacterTextSplitter

text = """
LangChain is a framework for developing applications powered by language models.
It provides tools for connecting LLMs to external data sources, integrating them with APIs,
and composing complex reasoning workflows.
"""

splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 80, 
    chunk_overlap = 20
    )

chunk = splitter.split_text(text)

for i,c in enumerate(chunk,1):
    print(f"Chunk No. {i}")
    print(c)
    print("*"*75)