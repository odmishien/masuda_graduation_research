import numpy as np
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn
import util

pd.set_option('display.max_columns', 10)

ids = []
all_data = []
bookmark_counts = []
nums_of_sentences = []
nums_of_comma = []
nums_of_period = []
lengths_of_text = []
distances_btw_commas = []
kanji_content_rates = []
sentiment_polarity_scores = []
raising_discussion_scores = []

for i in range(1, 4995):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            hot_masuda_objs = json.load(f)
        for masuda in hot_masuda_objs:
            bookmark_counts.append(int(masuda["bookmark_count"]))
            nums_of_sentences.append(masuda["num_of_sentences"])
            nums_of_comma.append(masuda["num_of_comma"])
            nums_of_period.append(masuda["num_of_period"])
            lengths_of_text.append(masuda["length_of_text"])
            distances_btw_commas.append(masuda["distance_btw_commas"])
            kanji_content_rates.append(masuda["kanji_content_rate"])
            sentiment_polarity_scores.append(
                masuda["sentiment_polarity_score"])
            raising_discussion_scores.append(
                masuda["raising_discussion_score"])
            ids.append(masuda["masuda_id"])

for i in range(2, 5001):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            bookmark_counts.append(int(masuda["bookmark_count"]))
            nums_of_sentences.append(masuda["num_of_sentences"])
            nums_of_comma.append(masuda["num_of_comma"])
            nums_of_period.append(masuda["num_of_period"])
            lengths_of_text.append(masuda["length_of_text"])
            distances_btw_commas.append(masuda["distance_btw_commas"])
            kanji_content_rates.append(masuda["kanji_content_rate"])
            sentiment_polarity_scores.append(
                masuda["sentiment_polarity_score"])
            raising_discussion_scores.append(
                masuda["raising_discussion_score"])
            ids.append(masuda["masuda_id"])

bookmark_counts = util.min_max(bookmark_counts)
nums_of_sentences = util.min_max(nums_of_sentences)
nums_of_comma = util.min_max(nums_of_comma)
nums_of_period = util.min_max(nums_of_period)
lengths_of_text = util.min_max(lengths_of_text)
distances_btw_commas = util.min_max(distances_btw_commas)
kanji_content_rates = util.min_max(kanji_content_rates)
sentiment_polarity_scores = util.min_max(sentiment_polarity_scores)
raising_discussion_scores = util.min_max(raising_discussion_scores)

for bc, ns, nc, np, lt, dbc, kcr, sps, rds in zip(bookmark_counts, nums_of_sentences, nums_of_comma, nums_of_period, lengths_of_text, distances_btw_commas, kanji_content_rates, sentiment_polarity_scores, raising_discussion_scores):
    all_data.append([
        bc, ns, nc, np, lt, dbc, kcr, sps, rds
    ])

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
        "sentiment_polarity_score",
        "raising_discussion_score"],
    index=ids)

print(df.corr())
seaborn.heatmap(df.corr())
plt.show()
