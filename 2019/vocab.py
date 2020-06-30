from gensim.models import word2vec
import numpy as np
import os

max_vals = []
min_vals = []
arrays = os.listdir('./arrays')
array_height = []
for array in arrays:
    nd_array = np.load("./arrays/" + array)
    array_height.append(nd_array.shape[0])
print(max(array_height))