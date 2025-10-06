from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
LangChain is a framework for building applications with large language models.
It provides components for retrieval, reasoning, and multi-agent orchestration.
Token-based splitting ensures your chunks fit inside model context windows.
"""

splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name = "gpt-4o-mini",
    chunk_size = 200,
    chunk_overlap = 40
)

chunk = splitter.split_text(text)

for i,c in enumerate(chunk,1):
    print(f"Chunk No. {i}")
    print(c)
    print("*"*75)
