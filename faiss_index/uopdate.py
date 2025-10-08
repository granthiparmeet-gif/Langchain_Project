from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os


load_dotenv()


pc = Pinecone()
embeddings = OpenAIEmbeddings()


index_name = "openai-demo"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print(f"✅ Index '{index_name}' created successfully!")

index = pc.Index(index_name)


texts = [
    "Artificial intelligence is transforming the world.",
    "Pinecone provides powerful vector databases.",
    "OpenAI creates state-of-the-art large language models.",
    "Pizza with extra cheese is my favorite food.",
    "Neural networks are a foundation of deep learning."
]
vectors = embeddings.embed_documents(texts)
ids = [f"id-{i}" for i in range(len(texts))]
metas = [{"text": t} for t in texts]


index.upsert(vectors=zip(ids, vectors, metas))
print(" Embeddings upserted successfully!")

index.update(
    id="id-0",
    set_metadata={"category": "Updated-AI", "text": "AI changing the world rapidly"}
)
print("Updated id-0 metadata successfully.")


query_text = "How is AI transforming technology?"
query_vector = embeddings.embed_query(query_text)

results = index.query(
    vector=query_vector, 
    top_k=3, 
    include_metadata=True,
    # filter = {"category":"AI"}
    )


print(f"\n Query: {query_text}\n")
for i, m in enumerate(results["matches"], 1):
    print(f"{i}. {m['metadata']['text']} ({m['score']:.3f})")
