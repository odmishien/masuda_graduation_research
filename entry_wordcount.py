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
pickle_path = './pickle/wordcount.pickle'

if not os.path.exists(pickle_path):
    for i in tqdm(range(2, 5001)):
        if os.path.exists("data/entry/masuda_{0}.json".format(i)):
            with open("data/entry/masuda_{0}.json".format(i), "r") as f:
                masuda_objs = json.load(f)
            for masuda in masuda_objs:
                if masuda["content"] is not None:
                    node = mecab.parseToNode(masuda["content"])
                    while node:
                        pos = node.feature.split(",")[0]
                        if pos == "名詞":
                            content.append(node.surface)
                        node = node.next

c = collections.Counter(content)
with open(pickle_path, "wb") as f:
    pickle.dump(c, f)
