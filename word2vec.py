from gensim.models import word2vec
import os

sentence = word2vec.Text8Corpus('wakati_masuda.txt')
model = word2vec.Word2Vec(sentence,size=100,min_count=1,window=5,iter=100)
model.save('masuda.model_2')