import json
import os

def get_bookmark(filename, counter):
    hot_entries = []
    if os.path.exists(filename):
        with open(filename, mode="r") as f:
            masuda_list = json.load(f)
        for masuda in masuda_list:
            if masuda["bookmark"] > 30:
                hot_entries.append(masuda)
    return hot_entries

if __name__ == "__main__":
    counter = 0
    hot_entries = []
    for page in range(2,30000):
        hot_entry = get_bookmark("data/masuda_{page}.json".format(page=page), counter)
        hot_entries.extend(hot_entry)
    with open('./data/hot_masuda.json', 'w') as f:
        json.dump(hot_entries, f, indent=2, ensure_ascii=False)
