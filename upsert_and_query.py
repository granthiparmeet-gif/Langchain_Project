from pinecone import Pinecone, ServerlessSpec
import numpy as np

pc = Pinecone(api_key="pcsk_5XChYQ_GH6HUPQwdV8i85gu2hWvx6qo2DAtWDSRDusqcqqAPWNHX1yx2fQZ86n2kkT4u4S")

index_name = "my-test-index"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print(f"Created index '{index_name}' successfully!")
index = pc.Index(index_name)


vectors = np.random.random((5,384)).tolist()
ids = [f"id-{i}" for i in range(5)]
metas = [{"topic": f"doc-{i}","source":"AI"} for i in range(5)]

index.upsert(vectors = zip (ids, vectors, metas))
print("The vectors are inserted successfully")

query = np.random.random((1,384)).tolist()[0]

results = index.query(vector=query, top_k=3, include_metadata=True)
print(results)