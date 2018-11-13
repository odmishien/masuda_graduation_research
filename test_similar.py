from gensim.models import word2vec

model = word2vec.Word2Vec.load("masuda.model_2")
results = model.wv.most_similar(positive=['本国'])
for result in results:
    print(result)