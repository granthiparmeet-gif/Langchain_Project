from pinecone import Pinecone, ServerlessSpec


index_name = "pinecone-demo-3"
pc =Pinecone(api_key="pcsk_5XChYQ_GH6HUPQwdV8i85gu2hWvx6qo2DAtWDSRDusqcqqAPWNHX1yx2fQZ86n2kkT4u4S")


if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric= "cosine",
        spec = ServerlessSpec(
            cloud = "aws",
            region="us-east-1"
        )
    )
    print(f"Index : {index_name} created successfully")

print("All Indexes : ", pc.list_indexes().names())

index = pc.Index(index_name)
print("Stats:", index.describe_index_stats())