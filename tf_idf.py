from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy
import json
import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
wakati_masudas = []


corpus = []
for i in range(2, 100):
    with open("data/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    for masuda in masuda_objs:
        wakati_masuda = {}
        node = mecab.parseToNode(masuda["text"])
        words = ""
        while node:
            pos = node.feature.split(",")[0]
            if pos == "名詞":
                words += node.surface + " "
            node = node.next
        wakati_masuda["id"] = masuda["id"]
        wakati_masuda["words"] = words
        corpus.append(wakati_masuda["words"])

vectorizer = TfidfVectorizer(max_df=0.9)
tfidfs = vectorizer.fit_transform(corpus)

# print('feature_names:', vectorizer.get_feature_names())

words = vectorizer.get_feature_names()
for doc_id, vec in zip(range(len(corpus)), tfidfs.toarray()):
    for w_id, tfidf in sorted(enumerate(vec), key=lambda x: x[1], reverse=True):
        lemma = words[w_id]
        # print('\t{0:s}: {1:f}'.format(lemma, tfidf))

cs = cosine_similarity(tfidfs.toarray(), tfidfs.toarray())
ics = numpy.argsort(cs)
print(ics)
for i, j in enumerate(ics):
    print("似ている文章A:")
    print(corpus[j[1]])
    print("似ている文章B:")
    print(corpus[i])
