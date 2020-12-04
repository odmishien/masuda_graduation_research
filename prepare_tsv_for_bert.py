import os
import json
from tqdm import tqdm
import csv

hot_results = []
not_hot_results = []
for i in tqdm(range(1, 4995)):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
            for masuda in masuda_objs:
                text = masuda["content"]
                text = text.replace('\n', '')
                bookmark_count = masuda["bookmark_count"]
                if int(bookmark_count) > 99:
                    hot_results.append([text, '1'])
                else:
                    not_hot_results.append([text, '0'])
    else:
        print(f'file not found {i}')
        continue

with open('data/for_bert/hot_entry.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerows(hot_results)

for i in tqdm(range(2, 5001)):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            text = masuda["content"]
            text = text.replace('\n', '')
            label = '0'
            bookmark_count = masuda["bookmark_count"]
            if int(bookmark_count) < 99 and len(text) > 300 and text.count('http://') < 1 and text.count('https://') < 1:
                not_hot_results.append([text, label])

with open('data/for_bert/entry.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerows(not_hot_results)
