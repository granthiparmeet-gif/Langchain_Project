#pcsk_5XChYQ_GH6HUPQwdV8i85gu2hWvx6qo2DAtWDSRDusqcqqAPWNHX1yx2fQZ86n2kkT4u4S

#region="us-east-1"


# from pinecone import Pinecone

# pc = Pinecone(api_key ="pcsk_5XChYQ_GH6HUPQwdV8i85gu2hWvx6qo2DAtWDSRDusqcqqAPWNHX1yx2fQZ86n2kkT4u4S")

# print("Indexes:", pc.list_indexes().names())

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="pcsk_5XChYQ_GH6HUPQwdV8i85gu2hWvx6qo2DAtWDSRDusqcqqAPWNHX1yx2fQZ86n2kkT4u4S")

index_name = "test-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )

    )

    print("Index created successfully")

print("Indexes: ", pc.list_indexes().names())

