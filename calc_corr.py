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

all_concat_df.bookmark_count = util.min_max(
    all_concat_df.bookmark_count.tolist())
all_concat_df.num_of_sentences = util.min_max(
    all_concat_df.num_of_sentences.tolist())
all_concat_df.num_of_comma = util.min_max(
    all_concat_df.num_of_comma.tolist())
all_concat_df.num_of_period = util.min_max(
    all_concat_df.num_of_period.tolist())
all_concat_df.num_of_exclamation_mark = util.min_max(
    all_concat_df.num_of_exclamation_mark.tolist())
all_concat_df.num_of_question_mark = util.min_max(
    all_concat_df.num_of_question_mark.tolist())
all_concat_df.length_of_text = util.min_max(
    all_concat_df.length_of_text.tolist())
all_concat_df.distance_btw_commas = util.min_max(
    all_concat_df.distance_btw_commas.tolist())
all_concat_df.kanji_content_rate = util.min_max(
    all_concat_df.kanji_content_rate.tolist())
# all_concat_df.sentiment_polarity_score = util.min_max(
#     all_concat_df.sentiment_polarity_score.tolist())
# all_concat_df.raising_discussion_score = util.min_max(
#     all_concat_df.raising_discussion_score.tolist())
# all_concat_df.highest_similarity = util.min_max(
#     all_concat_df.highest_similarity.tolist())
# all_concat_df.lowest_similarity = util.min_max(
#     all_concat_df.lowest_similarity.tolist())

show_columns = ["bookmark_count",
                "num_of_sentences", "num_of_comma", "num_of_period", "num_of_exclamation_mark", "num_of_question_mark", "length_of_text", "distance_btw_commas", "kanji_content_rate"]

print(all_concat_df[show_columns].corr())
seaborn.heatmap(all_concat_df[show_columns].corr())
plt.show()
