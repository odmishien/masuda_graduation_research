from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy
import json
import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
masudas = []

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
        corpus.append(words)
        masudas.append(masuda)

vectorizer = TfidfVectorizer(max_df=0.9)
tfidfs = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
cs = cosine_similarity(tfidfs.toarray(), tfidfs.toarray())
ics = numpy.argsort(-cs)

for i, j in enumerate(ics):
    top_similar_id = j[1]
    if cs[i][top_similar_id] > 0.7 and masudas[top_similar_id]["id"] != masudas[i]["id"]:
        print("id:{0}, ブクマ:{1}".format(
            masudas[top_similar_id]["id"], masudas[top_similar_id]["bookmark"]))
        print(masudas[top_similar_id]["text"])
        print("id:{0}, ブクマ:{1}".format(
            masudas[i]["id"], masudas[i]["bookmark"]))
        print(masudas[i]["text"])
        print("類似度: {0}".format(cs[i][top_similar_id]))
        print("-------------------------------------------")
