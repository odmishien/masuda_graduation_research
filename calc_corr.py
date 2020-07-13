import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn

pd.set_option('display.max_columns', 10)

ids = []
all_data = []

for i in range(1, 4995):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            hot_masuda_objs = json.load(f)
        for masuda in hot_masuda_objs:
            arr = [
                int(masuda["bookmark_count"]),
                masuda["num_of_sentences"],
                masuda["num_of_comma"],
                masuda["num_of_period"],
                masuda["length_of_text"],
                masuda["distance_btw_commas"],
                masuda["kanji_content_rate"],
                masuda["sentiment_polarity_score"]
            ]
            ids.append(masuda["masuda_id"])
            all_data.append(arr)

for i in range(2, 5001):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            arr = [
                int(masuda["bookmark_count"]),
                masuda["num_of_sentences"],
                masuda["num_of_comma"],
                masuda["num_of_period"],
                masuda["length_of_text"],
                masuda["distance_btw_commas"],
                masuda["kanji_content_rate"],
                masuda["sentiment_polarity_score"]
            ]
            ids.append(masuda["masuda_id"])
            all_data.append(arr)

df = pd.DataFrame(
    all_data,
    columns=[
        "bookmark_count",
        "num_of_sentences",
        "num_of_comma",
        "num_of_period",
        "length_of_text",
        "distance_btw_commas",
        "kanji_content_rate",
        "sentiment_polarity_score"],
    index=ids)

print(df.corr())
seaborn.heatmap(df.corr())
plt.show()
