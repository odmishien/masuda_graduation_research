from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import json
import MeCab
import itertools
from tqdm import tqdm
import os

corpusdir = "./model/"
file_w2v_model = corpusdir + "w2v_all_vector200_win5_sgns0.vec"

model = KeyedVectors.load_word2vec_format(
    file_w2v_model, binary=False)
mecab_path = os.getenv("MECAB_NEOLOGD_PATH")
mecab = MeCab.Tagger("-d {0}".format(mecab_path))


def calc_highest_and_lowest_similarity(nouns):
    patterns = list(itertools.combinations(nouns, 2))
    results = []
    for p in patterns:
        try:
            similarity = model.wv.similarity(p[0], p[1])
            results.append(similarity)
        except Exception as e:
            pass
    return max(results, default=0), min(results, default=0)


for i in tqdm(range(1, 4995)):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        updated_masuda_objs = []
        for masuda in masuda_objs:
            nouns = []
            if masuda["content"] is not None:
                node = mecab.parseToNode(masuda["content"])
                while node:
                    try:
                        pos = node.feature.split(",")[0]
                        if pos == "名詞":
                            nouns.append(node.surface)
                    except:
                        pass
                    node = node.next
            max_sim, min_sim = calc_highest_and_lowest_similarity(nouns)
            masuda["highest_similarity"] = str(max_sim)
            masuda["lowest_similarity"] = str(min_sim)
            updated_masuda_objs.append(masuda)
        with open('./data/hot_entry/masuda_{0}.json'.format(i), 'w') as f:
            json.dump(updated_masuda_objs, f, indent=2, ensure_ascii=False)

for i in tqdm(range(2, 5001)):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        updated_masuda_objs = []
        for masuda in masuda_objs:
            nouns = []
            if masuda["content"] is not None:
                node = mecab.parseToNode(masuda["content"])
                while node:
                    try:
                        pos = node.feature.split(",")[0]
                        if pos == "名詞":
                            nouns.append(node.surface)
                    except:
                        pass
                    node = node.next
            max_sim, min_sim = calc_highest_and_lowest_similarity(nouns)
            masuda["highest_similarity"] = str(max_sim)
            masuda["lowest_similarity"] = str(min_sim)
            updated_masuda_objs.append(masuda)
        with open('./data/entry/masuda_{0}.json'.format(i), 'w') as f:
            json.dump(updated_masuda_objs, f, indent=2, ensure_ascii=False)
