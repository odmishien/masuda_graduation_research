from gensim.models import word2vec
import os

sentence = word2vec.Text8Corpus('wakati_masuda_keiyoushi.txt')
model = word2vec.Word2Vec(sentence,size=100,min_count=1,window=5,sorted_vocab=1,sg=1)
model.save('model_keiyoushi_20190311')