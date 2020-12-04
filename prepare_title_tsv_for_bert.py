import os
import json
from tqdm import tqdm
import csv
from sklearn.model_selection import train_test_split
import unicodedata


def is_japanese(string):
    for ch in string:
        try:
            name = unicodedata.name(ch)
            if "CJK UNIFIED" in name or "HIRAGANA" in name or "KATAKANA" in name:
                return True
        except:
            return False
    return False


hot_results = []
for i in tqdm(range(1, 4995)):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            title = masuda["title"]
            label = '1'
            if title == '':
                continue
            if 'anond:' in title or 'http:' in title or 'https:' in title:
                continue
            if not is_japanese(title):
                continue
            hot_results.append([title, label])

hot_train_data, hot_test_data = train_test_split(hot_results, test_size=0.2)

not_hot_results = []
for i in tqdm(range(2, 5001)):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            title = masuda["title"]
            label = '0'
            if title == '':
                continue
            if 'anond:' in title or 'http:' in title or 'https:' in title:
                continue
            if not is_japanese(title):
                continue
            not_hot_results.append([title, label])

train_data, test_data = train_test_split(not_hot_results, test_size=0.2)

train_data = hot_train_data + train_data[:len(hot_train_data)]
test_data = hot_test_data + test_data[:len(hot_test_data)]

with open('data/for_bert/title_train.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerows(train_data)

with open('data/for_bert/title_test.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerows(test_data)
