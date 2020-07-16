from util import get_unique_elements_btw_list
import pickle

def pop_not_frequent_words(dic):
    for k, v in list(dic.items()):
        if v < 500:
            dic.pop(k, None)
    return dic

with open('pickle/hot_wordcount.pickle', "rb") as f:
    hot_wordcount = pickle.load(f)
with open('pickle/wordcount.pickle', "rb") as f:
    wordcount = pickle.load(f)

pop_hot_wordcount = pop_not_frequent_words(hot_wordcount)
pop_wordcount = pop_not_frequent_words(wordcount)

hot_unique_words = get_unique_elements_btw_list(pop_hot_wordcount.keys(), pop_wordcount.keys())

import pprint
pprint.pprint(hot_unique_words)
