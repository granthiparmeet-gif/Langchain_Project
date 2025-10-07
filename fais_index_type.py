import faiss
import numpy as np

dim = 384
num_vectors = 1000
query_k =5


vectors = np.random.random((num_vectors,dim)).astype("float32")

query = np.random.random((1, dim)).astype("float32")

print(f"\n✅ Data prepared: {num_vectors} vectors of dimension {dim}\n")

print("*"*60)

print(" Using IndexFlatL2 (exact search)")
index_flat = faiss.IndexFlatL2(dim)
index_flat.add(vectors)

D_flat , I_flat = index_flat.search(query, query_k)
print(f"Top-{query_k} results (IndexFlatL2):", I_flat[0], f"The distance is {D_flat}")

