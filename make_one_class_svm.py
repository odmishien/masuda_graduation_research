from sklearn.model_selection import train_test_split
from sklearn.svm import OneClassSVM
import os
import numpy as np
import matplotlib.pyplot as plt
import random

from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import json
import MeCab
import pickle

hot_masudas = []
masudas = []
vectors = []

pickle_path = './pickle/masudas.pickle'
if not os.path.exists(pickle_path):
    corpusdir = "./model/"
    file_w2v_model = corpusdir + "w2v_all_vector200_win5_sgns0.vec"

    model = KeyedVectors.load_word2vec_format(
        file_w2v_model, binary=False)
    mecab_path = os.getenv("MECAB_NEOLOGD_PATH")
    mecab = MeCab.Tagger("-d {0}".format(mecab_path))

    for i in range(1, 4995):
        if os.path.exists("data/hot_entry_no_noun_and_adj/masuda_{0}.json".format(i)):
            with open("data/hot_entry_no_noun_and_adj/masuda_{0}.json".format(i), "r") as f:
                hot_masuda_objs = json.load(f)
            for masuda in hot_masuda_objs:
                if masuda["content"] is not None:
                    node = mecab.parseToNode(masuda["content"])
                    sum_of_vector = 0
                    while node:
                        try:
                            sum_of_vector += model[node.surface]
                        except:
                            pass
                        node = node.next
                    if type(sum_of_vector) is not int:
                        vectors.append(sum_of_vector)
                        masudas.append(masuda)

    for i in range(2, 5001):
        with open("data/entry_no_noun_and_adj/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            if masuda["content"] is not None:
                node = mecab.parseToNode(masuda["content"])
                sum_of_vector = 0
                while node:
                    try:
                        sum_of_vector += model[node.surface]
                    except:
                        pass
                    node = node.next
                if type(sum_of_vector) is not int:
                    vectors.append(sum_of_vector)
                    masudas.append(masuda)
    with open(pickle_path, "wb") as f:
        pickle.dump(vectors, f)
else:
    with open(pickle_path, "rb") as f:
        vectors = pickle.load(f)

print("-----文章読み込み終わり-----")

# トレーニングデータ:テストデータ を 9:1 に分割
data_train, data_test = train_test_split(
    vectors, test_size=0.1, random_state=1)

clf = OneClassSVM(kernel='rbf', nu=0.2, gamma=0.001)
clf.fit(data_train)
# テストデータを分類器に入れる
pred = clf.predict(data_test)

index = np.where(pred < 0)
print(index)
# plt.scatter(data_test[:,0], data_test[:,1])
# plt.scatter(data_test[index, 0], data_test[index, 1], c='r', label='outlair')
# plt.legend()
# plt.savefig('OneClassSVM.png')
# plt.show()
