import json
import re
import os


def format_text(text):
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)  # URL文字列
    text = re.sub(r'[!-~]', "", text)  # 半角記号,数字,英字
    text = re.sub(r'[︰-＠]', "", text)  # 全角記号
    return text


def get_hot_entry(filename):
    hot_entries = []
    if os.path.exists(filename):
        with open(filename, mode="r") as f:
            masuda_list = json.load(f)
        for masuda in masuda_list:
            if masuda["bookmark"] > 30:
                masuda["text"] = format_text(masuda["text"])
                hot_entries.append(masuda)
    return hot_entries


if __name__ == "__main__":
    hot_entries = []
    for page in range(2, 5000):
        hot_entry = get_hot_entry("data/masuda_{page}.json".format(page=page))
        hot_entries.extend(hot_entry)
    with open('./data/hot_masuda.json', 'w') as f:
        json.dump(hot_entries, f, indent=2, ensure_ascii=False)
