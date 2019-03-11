import numpy
from gensim.models import word2vec
import os
import pickle
from janome.tokenizer import Tokenizer

t = Tokenizer()

def main():
    model = word2vec.Word2Vec.load("masuda.model_cbow")
    with open("./pickle/masuda.pickle","rb") as f:
        masuda_dict = pickle.load(f)
    entries = masuda_dict.keys()
    for i, entry in enumerate(entries):
        words = t.tokenize(entry, wakati=True)
        try:
            vec = text_to_vec(words, model)
            vec = normalize(vec)
            if masuda_dict[entry] > 0:
                pass
                # numpy.savetxt('./hot_vec/entry_' + str(i), vec)
            else:
                if len(vec) > 0:
                    numpy.savetxt('./not_hot_vec/entry_' + str(i), vec)
        except:
            pass
def text_to_vec(words, model):
    word_vecs = []
    for word in words:
        try:
            word_vecs.append(model[word])
        except:
            pass
    if len(word_vecs) == 0:
        return None
    text_vec = numpy.zeros(word_vecs[0].shape, dtype = word_vecs[0].dtype)
    for word_vec in word_vecs:
        text_vec = text_vec + word_vec
    return text_vec
def normalize(vec):
    return vec / numpy.linalg.norm(vec)
if __name__ == '__main__':
    main()