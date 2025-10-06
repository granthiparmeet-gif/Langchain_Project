from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

class TinyLoader(BaseLoader):
    def __init__(self, file_path : str):
        self.file_path = file_path

    def lazy_load(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            text = f.read()
        yield Document(page_content=text, metadata = {"source":self.file_path})


if __name__ == "__main__":
    loader = TinyLoader("sample.txt")

    for doc in loader.lazy_load():
        print("CONTENT:", doc.page_content[:100])
        print("METADATA:", doc.metadata)