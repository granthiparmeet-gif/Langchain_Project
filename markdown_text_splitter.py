from langchain_text_splitters import MarkdownTextSplitter


with open("sample.md", "r") as f:
    markdown_text = f.read()


splitter = MarkdownTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
)

chunks =splitter.split_text(markdown_text)

for c in chunks:
    print("=>", c)