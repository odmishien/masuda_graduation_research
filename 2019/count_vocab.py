from gensim.models import word2vec

model = word2vec.Word2Vec.load("masuda.model_cbow")
vocab = model.wv.vocab

with open('count_vocab.txt', mode='a') as f:
    for w in vocab.keys():
        count = str(vocab[w].count)
        f.write(w +"\n")
