import os
import json
from tqdm import tqdm
import csv

hot_results = []
for i in tqdm(range(1, 4995)):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            text = masuda["content"]
            label = '1'
            hot_results.append([text, label])

with open('data/for_bert/hot_entry.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerows(hot_results)

not_hot_results = []
for i in tqdm(range(2, 5001)):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            text = masuda["content"]
            label = '0'
            not_hot_results.append([text, label])

with open('data/for_bert/entry.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerows(not_hot_results)
