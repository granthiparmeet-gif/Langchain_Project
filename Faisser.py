# import faiss
# import numpy as np

# np.random.seed(42)

# num_vectors= 1000
# dim = 128
# query_k =6

# vectors = np.random.random((num_vectors, dim)).astype("float32")

# query = np.random.random((1,dim)).astype("float32")

# print(f"No of vectors : {vectors}\nNo of Dimension: {dim} ")

# print("Using the eucledian distance IndexFlatL2")

# ind = faiss.IndexFlatL2(dim)
# ind.add(vectors)

# D, I = ind.search(query, query_k)

# print("Top-5 indices:", I)
# print("Distances:", D)


# print ("Using index Flat IP Cosine")

# faiss.normalize_L2(vectors)
# faiss.normalize_L2(query)

# x = faiss.IndexFlatIP(dim)
# x.add(vectors)

# Dp, Ip = x.search(query, query_k)

# print("Top 5 Indices:", Ip)
# print("Distances", Dp)


# print("using Index IVFFlat")

# quant = faiss.IndexFlatL2(dim)

# nlist =50
# ind_ivf = faiss.IndexIVFFlat(quant,dim,nlist)

# ind_ivf.train(vectors)
# ind_ivf.add(vectors)
# # ind_ivf.nprobe= 5

# D_ivf, I_ivf = ind_ivf.search (query, query_k)

# print("Top-5 indices:", I_ivf)
# print("Distances:", D_ivf)


# print("Cluster using IVFPQ")

# quan_ivfpq = faiss.IndexFlatL2(dim)

# nlist = 50
# m=8
# nbits =8

# index_ivfpq = faiss.IndexIVFPQ(quan_ivfpq, dim, nlist, m, nbits)

# index_ivfpq.train(vectors)
# index_ivfpq.add(vectors)
# index_ivfpq.nprobe=5
# Dv, Iv= index_ivfpq.search(query, query_k)
# print("Top-5 indices:", Iv)
# print("Distances:", Dv)


# print("Learning Index HNSW")


# index_hnsw = faiss.IndexHNSWFlat(dim, 32)
# index_hnsw.add(vectors)

# D_hnsw,I_hnsw = index_hnsw.search(query,query_k)

# print("Top-5 indices:", I_hnsw)
# print("Distances:", D_hnsw)


print("Saving and loading Index")

import faiss
import numpy as np
import os

num_vectors =1000
dim=128
nlist =50
np.random.seed(42)

vectors = np.random.random((num_vectors,dim)).astype("float32")
query = np.random.random((num_vectors,dim)).astype("float32")


quantizer = faiss.IndexFlatL2(dim)
index_ivf = faiss.IndexIVFFlat(quantizer, dim, nlist)

index_ivf.train(vectors)
index_ivf.add(vectors)

index_ivf.nprobe = 8

D_index_ivf, I_index_ivf = index_ivf.search(query, 5)

print (D_index_ivf, I_index_ivf)


save_path = "faiss_index-ivf"
faiss.write_index(index_ivf, save_path)

print(f"Index saved to {save_path}")

index_load = faiss.read_index(save_path)
print("Index loaded successfully")