import numpy as np
import sys

embedding_path = 'data/embed/counter-fitted-vectors.txt'

embeddings = []
with open(embedding_path, 'r') as ifile:
    for line in ifile:
        embedding = [float(num) for num in line.strip().split()[1:]]
        embeddings.append(embedding)
embeddings = np.array(embeddings)
print(embeddings.T.shape)
norm = np.linalg.norm(embeddings, axis=1, keepdims=True)
embeddings = np.asarray(embeddings / norm, "float32")
product = np.dot(embeddings, embeddings.T)
np.save(('cos_sim_counter_fitting.npy'), product)
