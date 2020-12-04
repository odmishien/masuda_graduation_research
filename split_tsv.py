import csv
import sys
from sklearn.model_selection import train_test_split

maxInt = sys.maxsize
csv.field_size_limit(maxInt)

with open('data/for_bert/hot_entry.tsv', mode='r', newline='', encoding='utf-8') as f:
    tsv_reader = csv.reader(f, delimiter='\t')
    read_data = [row for row in tsv_reader]

hot_train_data, hot_test_data = train_test_split(read_data, test_size=0.2)

with open('data/for_bert/entry.tsv', mode='r', newline='', encoding='utf-8') as f:
    tsv_reader = csv.reader(f, delimiter='\t')
    read_data = [row for row in tsv_reader]

train_data, test_data = train_test_split(read_data, test_size=0.2)

train_data = hot_train_data[:len(train_data)] + train_data
test_data = hot_test_data[:len(test_data)] + test_data

header = ["text", "label"]

with open('data/for_bert/train_20201111.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    # tsv_writer.writerow(header)
    tsv_writer.writerows(train_data)

with open('data/for_bert/test_20201111.tsv', mode='w', newline='', encoding='utf-8') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    # tsv_writer.writerow(header)
    tsv_writer.writerows(test_data)
