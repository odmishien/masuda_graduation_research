from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy
import json
import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
hot_masudas = []
masudas = []
hot_corpus = []
corpus = []

with open("data/hot_masuda.json", "r") as f:
    hot_masuda_objs = json.load(f)
for masuda in hot_masuda_objs:
    wakati_masuda = {}
    node = mecab.parseToNode(masuda["text"])
    words = ""
    while node:
        pos = node.feature.split(",")[0]
        if pos == "名詞":
            words += node.surface + " "
        node = node.next
    hot_corpus.append(words)
    hot_masudas.append(masuda)

for i in range(4220, 5000):
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
        corpus.append(words)
        masudas.append(masuda)

vectorizer = TfidfVectorizer(max_df=0.9)
tfidfs = vectorizer.fit_transform(corpus)

for i, hc in enumerate(hot_corpus):
    hc_vector = vectorizer.transform([hc])
    cs = cosine_similarity(hc_vector.toarray(), tfidfs.toarray())
    ics = numpy.argsort(-cs)
    top_3_similar_index = ics[0, 1:4]
    print("id:{0}, ブクマ:{1}".format(
        hot_masudas[i]["id"], hot_masudas[i]["bookmark"]))
    print(hot_masudas[i]["text"])
    print("-------------------------------------------")
    print("👑似てるエントリランキング👑")
    for rank, j in enumerate(top_3_similar_index):
        print("第{0}位".format(rank + 1))
        print("id:{0}, ブクマ:{1}".format(
            masudas[j]["id"], masudas[j]["bookmark"]))
        print(masudas[j]["text"])
        print("類似度: {0}".format(cs[0, j]))
        print("-------------------------------------------")
