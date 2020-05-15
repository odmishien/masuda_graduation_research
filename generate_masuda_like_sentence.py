import markovify
import MeCab
import json


mecab = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
parsed_text = ""

for i in range(1, 344):
    with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
        hot_masuda_objs = json.load(f)
    for masuda in hot_masuda_objs:
        if masuda["content"] is not None:
            words = mecab.parse(masuda["content"])
            words = words.rstrip('\n')
            parsed_text += words
            parsed_text += '\n'

text_model = markovify.NewlineText(parsed_text, state_size=3)

for _ in range(10):
    sentence = text_model.make_sentence(tries=100)
    if sentence is not None:
        print(sentence.replace(' ', ''))
