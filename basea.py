from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from typing import List


class SimpleRetriever(BaseRetriever):
    """A naive retriever that always returns the first k docs"""
    
    docs: List[Document]  # Declare as model field
    k: int = 2            # Default value is allowed
    
    def _get_relevant_documents(self, query: str) -> List[Document]:
        print(f"Query received: {query}")
        return self.docs[: self.k]

docs = [Document(page_content=f"This is doc {i}") for i in range(5)]

# Instantiate retriever
retriever = SimpleRetriever(docs=docs, k=3)

# Test the retriever
print(retriever.invoke("Any question"))