from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy
import json

with open("data/wakati_hot_masuda.json", "r") as f:
    wakati_masudas = json.load(f)
corpus = []
for wakati_masuda in wakati_masudas:
    corpus.append(wakati_masuda["words"])

vectorizer = TfidfVectorizer(max_df=0.9)
tfidfs = vectorizer.fit_transform(corpus)

# print('feature_names:', vectorizer.get_feature_names())

words = vectorizer.get_feature_names()
for doc_id, vec in zip(range(len(corpus)), tfidfs.toarray()):
    print('doc_id:', doc_id)
    for w_id, tfidf in sorted(enumerate(vec), key=lambda x: x[1], reverse=True):
        lemma = words[w_id]
        # print('\t{0:s}: {1:f}'.format(lemma, tfidf))

cs = cosine_similarity(tfidfs.toarray(), tfidfs.toarray())
for c in numpy.nditer(cs.T):
    sorted_index = numpy.argsort(c)
    print(c)

