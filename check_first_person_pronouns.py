import pprint
import pandas as pd
import numpy as np
import MeCab
import os
import seaborn
import matplotlib.pyplot as plt
import japanize_matplotlib

mecab_path = os.getenv("MECAB_NEOLOGD_PATH")
mecab = MeCab.Tagger("-d {0}".format(mecab_path))

first_person_pronouns = ['俺', 'わたし', '私', '僕', 'ボク', 'あたし', 'オレ', 'おれ', '己', 'わい',
                         'オイラ', 'ぼく', 'わたくし', 'あたしゃ', '余', 'おいら', 'わたしゃ', 'おら', '吾輩', '小生', 'ウチ', 'あたい']
pos_nega_noun_count = pd.DataFrame(
    data=np.zeros_like(np.arange(len(first_person_pronouns) * 2).reshape(len(first_person_pronouns), 2)), index=first_person_pronouns, columns=['positive', 'negative'])
df = pd.read_table('./data/for_bert/train_20201111.tsv')
print('文書数')
print(len(df.query('label == 1')))
print(len(df.query('label == 0')))
for i, row in df.iterrows():
    try:
        node = mecab.parseToNode(row['text'])
        while node:
            if node.surface in first_person_pronouns:
                if row['label']:
                    pos_nega_noun_count.at[node.surface, 'positive'] += 1
                else:
                    pos_nega_noun_count.at[node.surface, 'negative'] += 1
                break
            node = node.next
    except:
        print(row['text'])

pos_nega_noun_count.reset_index(inplace=True)
pos_nega_noun_count = pd.melt(
    pos_nega_noun_count, id_vars='index', var_name="label", value_name="count")
print('一人称が出てきた文書数')
print('positive:')
print(pos_nega_noun_count[pos_nega_noun_count['label']
                          == 'positive']['count'].sum())
print('nagative:')
print(pos_nega_noun_count[pos_nega_noun_count['label']
                          == 'negative']['count'].sum())

seaborn.catplot(data=pos_nega_noun_count, x='index',
                y='count', hue='label', kind='bar')
plt.show()
