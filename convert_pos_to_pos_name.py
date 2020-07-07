import json
import MeCab
import os

mecab_path = os.getenv("MECAB_NEOLOGD_PATH")
mecab = MeCab.Tagger("-d {0}".format(mecab_path))

for i in range(1, 5000):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)) and not os.path.exists('./data/hot_entry_no_noun_and_adj/masuda_{page}.json'.format(page=i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            hot_masuda_objs = json.load(f)
        converted_hot_masuda_objs = []
        for masuda in hot_masuda_objs:
            if masuda["content"] is not None:
                content = ""
                node = mecab.parseToNode(masuda["content"])
                while node:
                    pos = node.feature.split(",")[0]
                    if pos == "名詞":
                        content += "名詞"
                    elif pos == "形容詞":
                        content += "形容詞"
                    else:
                        content += node.surface
                    node = node.next
                masuda["content"] = content
            converted_hot_masuda_objs.append(masuda)
        with open('./data/hot_entry_no_noun_and_adj/masuda_{page}.json'.format(page=i), 'w') as f:
            json.dump(converted_hot_masuda_objs, f, indent=2, ensure_ascii=False)

for i in range(2, 5001):
    with open("data/entry/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    converted_masuda_objs = []
    for masuda in masuda_objs:
        if masuda["content"] is not None:
            content = ""
            node = mecab.parseToNode(masuda["content"])
            while node:
                pos = node.feature.split(",")[0]
                if pos == "名詞":
                    content += "名詞"
                elif pos == "形容詞":
                    content += "形容詞"
                else:
                    content += node.surface
                node = node.next
            masuda["content"] = content
        converted_masuda_objs.append(masuda)
    with open('./data/entry_no_noun_and_adj/masuda_{page}.json'.format(page=i), 'w') as f:
        json.dump(converted_masuda_objs, f, indent=2, ensure_ascii=False)
