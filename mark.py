from langchain_text_splitters import MarkdownHeaderTextSplitter


headers_to_split = [
    ("#","Header1"),
    ("##", "Header2"),
    ("###", "Header3")
]

with open("sample.md", "r") as f:
    markdown_text = f.read()

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split)

docs = splitter.split_text(markdown_text)

for doc in docs:
    print(doc.page_content)
    print("Metadata:", doc.metadata)
    print("-"*60)