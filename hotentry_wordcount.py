import os
import json
import pickle
import collections
from tqdm import tqdm

import MeCab
import matplotlib.pyplot as plt

mecab_path = os.getenv("MECAB_NEOLOGD_PATH")
mecab = MeCab.Tagger("-d {0}".format(mecab_path))
content = []
pickle_path = './pickle/hot_wordcloud.pickle'

if not os.path.exists(pickle_path):
    for i in tqdm(range(1, 5000)):
        if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
            with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
                hot_masuda_objs = json.load(f)
            for masuda in hot_masuda_objs:
                if masuda["content"] is not None:
                    node = mecab.parseToNode(masuda["content"])
                    while node:
                        pos = node.feature.split(",")[0]
                        if pos == "名詞":
                            content.append(node.surface)
                        node = node.next
else:
    with open(pickle_path, "rb") as f:
        content = pickle.load(f)

c = collections.Counter(content)
with open(pickle_path, "wb") as f:
    pickle.dump(c, f)
