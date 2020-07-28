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
nums_of_exclamation_mark = []
nums_of_question_mark = []
lengths_of_text = []
distances_btw_commas = []
kanji_content_rates = []
sentiment_polarity_scores = []
raising_discussion_scores = []
include_haikei_labels = []
include_riyuu_labels = []
include_himitsu_labels = []
include_naze_labels = []
include_uragawa_labels = []
include_shinzitsu_labels = []
include_shirarezaru_labels = []
include_zittai_labels = []
include_housoku_labels = []
include_tukurikata_labels = []
include_houhou_labels = []
include_hiketsu_labels = []
include_sugoi_labels = []
include_sugo_labels = []
include_odoroki_labels = []
include_suteki_labels = []
include_bikkuri_labels = []
include_tokubetsu_labels = []
include_special_labels = []
include_totteoki_labels = []
include_dakeno_labels = []

for i in range(1, 4995):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            hot_masuda_objs = json.load(f)
        for masuda in hot_masuda_objs:
            bookmark_counts.append(int(masuda["bookmark_count"]))
            nums_of_sentences.append(masuda["num_of_sentences"])
            nums_of_comma.append(masuda["num_of_comma"])
            nums_of_period.append(masuda["num_of_period"])
            nums_of_exclamation_mark.append(masuda["num_of_exclamation_mark"])
            nums_of_question_mark.append(masuda["num_of_question_mark"])
            lengths_of_text.append(masuda["length_of_text"])
            distances_btw_commas.append(masuda["distance_btw_commas"])
            kanji_content_rates.append(masuda["kanji_content_rate"])
            sentiment_polarity_scores.append(
                masuda["sentiment_polarity_score"])
            raising_discussion_scores.append(
                masuda["raising_discussion_score"])
            ids.append(masuda["masuda_id"])
            include_bikkuri_labels.append(masuda["is_include_bikkuri"])
            include_dakeno_labels.append(masuda["is_include_dakeno"])
            include_haikei_labels.append(masuda["is_include_haikei"])
            include_hiketsu_labels.append(masuda["is_include_hiketsu"])
            include_himitsu_labels.append(masuda["is_include_himitsu"])
            include_houhou_labels.append(masuda["is_include_houhou"])
            include_housoku_labels.append(masuda["is_include_housoku"])
            include_naze_labels.append(masuda["is_include_naze"])
            include_odoroki_labels.append(masuda["is_include_odoroki"])
            include_riyuu_labels.append(masuda["is_include_riyuu"])
            include_shinzitsu_labels.append(masuda["is_include_shinzitsu"])
            include_shirarezaru_labels.append(masuda["is_include_shirarezaru"])
            include_special_labels.append(masuda["is_include_special"])
            include_sugo_labels.append(masuda["is_include_sugo"])
            include_sugoi_labels.append(masuda["is_include_sugoi"])
            include_suteki_labels.append(masuda["is_include_suteki"])
            include_tokubetsu_labels.append(masuda["is_include_tokubetsu"])
            include_totteoki_labels.append(masuda["is_include_totteoki"])
            include_tukurikata_labels.append(masuda["is_include_tukurikata"])
            include_uragawa_labels.append(masuda["is_include_uragawa"])
            include_zittai_labels.append(masuda["is_include_zittai"])


for i in range(2, 5001):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        for masuda in masuda_objs:
            bookmark_counts.append(int(masuda["bookmark_count"]))
            nums_of_sentences.append(masuda["num_of_sentences"])
            nums_of_comma.append(masuda["num_of_comma"])
            nums_of_period.append(masuda["num_of_period"])
            nums_of_exclamation_mark.append(masuda["num_of_exclamation_mark"])
            nums_of_question_mark.append(masuda["num_of_question_mark"])
            lengths_of_text.append(masuda["length_of_text"])
            distances_btw_commas.append(masuda["distance_btw_commas"])
            kanji_content_rates.append(masuda["kanji_content_rate"])
            sentiment_polarity_scores.append(
                masuda["sentiment_polarity_score"])
            raising_discussion_scores.append(
                masuda["raising_discussion_score"])
            ids.append(masuda["masuda_id"])
            include_bikkuri_labels.append(masuda["is_include_bikkuri"])
            include_dakeno_labels.append(masuda["is_include_dakeno"])
            include_haikei_labels.append(masuda["is_include_haikei"])
            include_hiketsu_labels.append(masuda["is_include_hiketsu"])
            include_himitsu_labels.append(masuda["is_include_himitsu"])
            include_houhou_labels.append(masuda["is_include_houhou"])
            include_housoku_labels.append(masuda["is_include_housoku"])
            include_naze_labels.append(masuda["is_include_naze"])
            include_odoroki_labels.append(masuda["is_include_odoroki"])
            include_riyuu_labels.append(masuda["is_include_riyuu"])
            include_shinzitsu_labels.append(masuda["is_include_shinzitsu"])
            include_shirarezaru_labels.append(masuda["is_include_shirarezaru"])
            include_special_labels.append(masuda["is_include_special"])
            include_sugo_labels.append(masuda["is_include_sugo"])
            include_sugoi_labels.append(masuda["is_include_sugoi"])
            include_suteki_labels.append(masuda["is_include_suteki"])
            include_tokubetsu_labels.append(masuda["is_include_tokubetsu"])
            include_totteoki_labels.append(masuda["is_include_totteoki"])
            include_tukurikata_labels.append(masuda["is_include_tukurikata"])
            include_uragawa_labels.append(masuda["is_include_uragawa"])
            include_zittai_labels.append(masuda["is_include_zittai"])

bookmark_counts = util.min_max(bookmark_counts)
nums_of_sentences = util.min_max(nums_of_sentences)
nums_of_comma = util.min_max(nums_of_comma)
nums_of_period = util.min_max(nums_of_period)
nums_of_exclamation_mark = util.min_max(nums_of_exclamation_mark)
nums_of_question_mark = util.min_max(nums_of_question_mark)
lengths_of_text = util.min_max(lengths_of_text)
distances_btw_commas = util.min_max(distances_btw_commas)
kanji_content_rates = util.min_max(kanji_content_rates)
sentiment_polarity_scores = util.min_max(sentiment_polarity_scores)
raising_discussion_scores = util.min_max(raising_discussion_scores)

for bc, ns, nc, np, ne, nq, lt, dbc, kcr, sps, rds, bikkuri, dakeno, haikei, hiketsu, himitsu, houhou, housoku, naze, odoroki, riyuu, shinzitsu, shirarezaru, special, sugo, sugoi, suteki, tokubetsu, totteoki, tukurikata, uragawa, zittai in zip(bookmark_counts, nums_of_sentences, nums_of_comma, nums_of_period, nums_of_exclamation_mark, nums_of_question_mark, lengths_of_text, distances_btw_commas, kanji_content_rates, sentiment_polarity_scores, raising_discussion_scores, include_bikkuri_labels, include_dakeno_labels, include_haikei_labels, include_hiketsu_labels, include_himitsu_labels, include_houhou_labels, include_housoku_labels, include_naze_labels, include_odoroki_labels, include_riyuu_labels, include_shinzitsu_labels, include_shirarezaru_labels, include_special_labels, include_sugo_labels, include_sugoi_labels, include_suteki_labels, include_tokubetsu_labels, include_totteoki_labels, include_tukurikata_labels, include_uragawa_labels, include_zittai_labels):
    all_data.append([
        bc, ns, nc, np, ne, nq, lt, dbc, kcr, sps, rds, bikkuri, dakeno, haikei, hiketsu, himitsu, houhou, housoku, naze, odoroki, riyuu, shinzitsu, shirarezaru, special, sugo, sugoi, suteki, tokubetsu, totteoki, tukurikata, uragawa, zittai
    ])

df = pd.DataFrame(
    all_data,
    columns=[
        "bookmark_count",
        "num_of_sentences",
        "num_of_comma",
        "num_of_period",
        "num_of_exclamation_mark",
        "num_of_question_mark",
        "length_of_text",
        "distance_btw_commas",
        "kanji_content_rate",
        "sentiment_polarity_score",
        "raising_discussion_score",
        "include_bikkuri_labels", "include_dakeno_labels", "include_haikei_labels", "include_hiketsu_labels", "include_himitsu_labels", "include_houhou_labels", "include_housoku_labels", "include_naze_labels", "include_odoroki_labels", "include_riyuu_labels", "include_shinzitsu_labels", "include_shirarezaru_labels", "include_special_labels", "include_sugo_labels", "include_sugoi_labels", "include_suteki_labels", "include_tokubetsu_labels", "include_totteoki_labels", "include_tukurikata_labels", "include_uragawa_labels", "include_zittai_labels", ],
    index=ids)

print(df.corr())
seaborn.heatmap(df.corr())
plt.show()
