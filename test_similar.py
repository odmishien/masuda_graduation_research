from gensim.models import word2vec

model = word2vec.Word2Vec.load("masuda.model")
results = model.wv.most_similar(positive=['お父さん'])
for result in results:
    print(result)