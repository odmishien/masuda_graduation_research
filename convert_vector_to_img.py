from gensim.models import word2vec
import numpy as np
import os

# max:9.400702 min:-10.083586

new_max = 255
new_min = 0
old_max = 9.400702
old_min = -10.083586
max_height = 4168

entries = os.listdir('./entries')

model = word2vec.Word2Vec.load("masuda.model_2")
vocab = model.wv.vocab
for entry in entries:
    with open('./entries/' + entry) as f:
        words = f.read()
    words = words.split()
    nd_array = np.empty((0,100), int)
    for w in words:
        old_val = model[w]
        new_val = (new_max - new_min) * (old_val - old_min) / (old_max - old_min) + new_min
        nd_array = np.append(nd_array, np.array([new_val]), axis=0)
    while nd_array.shape[0] < max_height:
        nd_array = np.append(nd_array, 0)
    print(nd_array)
    np.save('./arrays/'+ entry , nd_array)
# # for v in vocab:
# #     nd_array = model[v]
# #     new_val = (new_max - new_min) * (nd_array - old_min) / (old_max - old_min) + new_min
