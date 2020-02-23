from gensim.models import word2vec

pos = str(input("元の単語："))
neg = str(input("引きたい単語："))
model = word2vec.Word2Vec.load("masuda.model")
vocab = model.wv.vocab
results = model.wv.most_similar(positive=[pos],negative=[neg])
for result in results:
    print(result)