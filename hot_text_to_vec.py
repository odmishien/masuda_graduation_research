import numpy
from gensim.models import word2vec
import os
import codecs

def main():
    model = word2vec.Word2Vec.load("model_keiyoushi_20190311")
    entries = os.listdir('./normal_keiyoushi_entries')
    for entry in entries:
        f = codecs.open('./normal_keiyoushi_entries/'+entry, 'r', 'utf-8', 'ignore')
        for line in f:
            words = line.rstrip().split(' ')
            try:
                vec = text_to_vec(words, model)
                if len(vec) > 0:
                    numpy.savetxt('./normal_vec_keiyoushi/' + entry, vec)
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
# def normalize(vec):
#     return vec / numpy.linalg.norm(vec)
if __name__ == '__main__':
    main()