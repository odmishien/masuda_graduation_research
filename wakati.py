import MeCab
import json

with open("data/hot_masuda.json", "r") as f:
    masuda_objs = json.load(f)

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
wakati_masudas = []
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
    wakati_masudas.append(wakati_masuda)
with open('data/wakati_hot_masuda.json', 'w') as f:
    json.dump(wakati_masudas, f, indent=2, ensure_ascii=False)
