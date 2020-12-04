import numpy as np
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn
import util

pd.set_option('display.max_columns', 10)

hot_concat = []
for i in range(1, 4995):
    if os.path.exists(f'data/hot_entry/masuda_{i}.json'):
        hot_df = pd.read_json(f'data/hot_entry/masuda_{i}.json')
        hot_concat.append(hot_df)
hot_concat_df = pd.concat(hot_concat)

not_hot_concat = []
for i in range(2, 5001):
    if os.path.exists(f'data/entry/masuda_{i}.json'):
        not_hot_df = pd.read_json(f'data/entry/masuda_{i}.json')
        not_hot_concat.append(not_hot_df)
not_hot_concat_df = pd.concat(not_hot_concat)

all_concat_df = pd.concat([hot_concat_df, not_hot_concat_df])

all_concat_df.bookmark_counts = util.min_max(
    all_concat_df.bookmark_counts.tolist())
all_concat_df.nums_of_sentences = util.min_max(
    all_concat_df.nums_of_sentences.tolist())
all_concat_df.nums_of_comma = util.min_max(
    all_concat_df.nums_of_comma.tolist())
all_concat_df.nums_of_period = util.min_max(
    all_concat_df.nums_of_period.tolist())
all_concat_df.nums_of_exclamation_mark = util.min_max(
    all_concat_df.nums_of_exclamation_mark.tolist())
all_concat_df.nums_of_question_mark = util.min_max(
    all_concat_df.nums_of_question_mark.tolist())
all_concat_df.lengths_of_text = util.min_max(
    all_concat_df.lengths_of_text.tolist())
all_concat_df.distances_btw_commas = util.min_max(
    all_concat_df.distances_btw_commas.tolist())
all_concat_df.kanji_content_rates = util.min_max(
    all_concat_df.kanji_content_rates.tolist())
all_concat_df.sentiment_polarity_scores = util.min_max(
    all_concat_df.sentiment_polarity_scores.tolist())
all_concat_df.raising_discussion_scores = util.min_max(
    all_concat_df.raising_discussion_scores.tolist())
all_concat_df.highest_similarities = util.min_max(
    all_concat_df.highest_similarities.tolist())
all_concat_df.lowest_similarities = util.min_max(
    all_concat_df.lowest_similarities.tolist())

print(all_concat_df.corr())
seaborn.heatmap(all_concat_df.corr())
plt.show()
