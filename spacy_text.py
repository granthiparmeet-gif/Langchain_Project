from langchain_text_splitters import SpacyTextSplitter

text = """
LangChain enables structured AI applications. SpaCy understands language syntax and meaning.
This splitter uses SpaCy to break paragraphs into meaningful sentences.
"""

splitter = SpacyTextSplitter(chunk_size=80, chunk_overlap=20)
chunks = splitter.split_text(text)

for i, c in enumerate(chunks, 1):
    print(f"Chunk {i}: {c}")
