from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="pcsk_5XChYQ_GH6HUPQwdV8i85gu2hWvx6qo2DAtWDSRDusqcqqAPWNHX1yx2fQZ86n2kkT4u4S")


index_name = "developer-quick-start"

if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model": "llama-text-embed-v2",
            "field_map": {"text": "chunk_text"}
        }
    )
    print(f"✅ Index '{index_name}' created and linked to Llama embeddings!")

index = pc.Index(index_name)
print("Index ready:", index_name)   