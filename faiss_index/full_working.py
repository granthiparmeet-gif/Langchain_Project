from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

open_ai = OpenAI()
pc=Pinecone()

index_name= "openai-demo"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region = "us-east-1")
    )

    print(f"Index created successfully{index_name}")

index = pc.Index(index_name)

texts = [
    "Artificial intelligence is transforming the world.",
    "Pinecone provides powerful vector databases.",
    "OpenAI creates state-of-the-art large language models.",
    "Pizza with extra cheese is my favorite food.",
    "Neural networks are a foundation of deep learning."
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectors = embeddings.embed_documents(texts)

ids = [f"id-{i}" for i in range(len(texts))]
metas = [{"text": t} for t in texts]

index.upsert(vectors=zip(ids,vectors, metas))
print("Embeddings upserted successfully")

query_text = "How is AI transforming technology?"
query_vector = embeddings.embed_query(query_text)

results = index.query(vector=query_vector, top_k=3, include_metadata=True)

print(f"Query: {query_text}")

for m in results["matches"]:
    print(f"{m['metadata']['text']} = {m['score']}")