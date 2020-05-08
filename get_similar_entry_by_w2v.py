from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import numpy
import json
import MeCab

corpusdir = "./model/"
file_w2v_model = corpusdir + "w2v_all_vector200_win5_sgns0.vec"

model = KeyedVectors.load_word2vec_format(
    file_w2v_model, binary=False)

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
hot_masudas = []
masudas = []
hot_vectors = []
vectors = []

for i in range(1, 344):
    with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
        hot_masuda_objs = json.load(f)
    for masuda in hot_masuda_objs:
        wakati_masuda = {}
        node = mecab.parseToNode(masuda["content"])
        sum_of_vector = 0
        while node:
            pos = node.feature.split(",")[0]
            if pos == "名詞":
                try:
                    sum_of_vector += model[node.surface]
                except:
                    pass
            node = node.next
        hot_vectors.append(sum_of_vector)
        hot_masudas.append(masuda)

for i in range(2, 5001):
    with open("data/entry/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    for masuda in masuda_objs:
        wakati_masuda = {}
        node = mecab.parseToNode(masuda["content"])
        sum_of_vector = 0
        while node:
            pos = node.feature.split(",")[0]
            if pos == "名詞":
                try:
                    sum_of_vector += model[node.surface]
                except:
                    pass
            node = node.next
        vectors.append(sum_of_vector)
        masudas.append(masuda)

for i, vec in enumerate(hot_vectors):
    nearest_index = get_nearest_index_of_value(vectors, vec)
    print("\n")
    print("id:{0}, ブクマ:{1}".format(
        hot_masudas[i]["masuda_id"], hot_masudas[i]["bookmark_count"]))
    print(hot_masudas[i]["content"])
    print("\n")
    print("👑似てるエントリ👑")
    print("id:{0}, ブクマ:{1}".format(
        masudas[nearest_index]["masuda_id"], masudas[nearest_index]["bookmark_count"]))
    print(masudas[nearest_index]["content"])
    print("ホットエントリのvector:{0}".format(vec))
    print("似ているエントリのvector:{0}".format(vectors[nearest_index]))
    print("-------------------------------------------")


def get_nearest_index_of_value(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = numpy.abs(numpy.asarray(list) - num).argmin()
    return idx
