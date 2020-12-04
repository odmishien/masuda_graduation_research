import pandas as pd

df = pd.read_table('data/for_bert/train_20201111.tsv')
df = df.query('label == 1')
for i, row in df.iterrows():
    if len(row['text']) < 50:
        print(row['text'])
