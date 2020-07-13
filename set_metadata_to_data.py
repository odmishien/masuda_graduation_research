import os
import json
import util
from tqdm import tqdm

for i in tqdm(range(1, 4995)):
    if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
        with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
            hot_masuda_objs = json.load(f)
        result = []
        for masuda in hot_masuda_objs:
            text = masuda["content"]
            if text is not None:
                masuda["num_of_sentences"] = util.get_num_of_sentences(text)
                masuda["num_of_comma"] = util.get_num_of_comma(text)
                masuda["num_of_period"] = util.get_num_of_period(text)
                masuda["length_of_text"] = util.get_length_of_text(text)
                masuda["distance_btw_commas"] = util.get_distance_btw_commas(text)
                masuda["kanji_content_rate"] = util.get_kanji_content_rate(text)
                masuda["sentiment_polarity_score"] = util.get_sentiment_polarity_score(text)
                result.append(masuda)
        with open("data/hot_entry/masuda_{0}.json".format(i), "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

for i in tqdm(range(2, 5001)):
    if os.path.exists("data/entry/masuda_{0}.json".format(i)):
        with open("data/entry/masuda_{0}.json".format(i), "r") as f:
            masuda_objs = json.load(f)
        result = []
        for masuda in masuda_objs:
            text = masuda["content"]
            if text is not None:
                masuda["num_of_sentences"] = util.get_num_of_sentences(text)
                masuda["num_of_comma"] = util.get_num_of_comma(text)
                masuda["num_of_period"] = util.get_num_of_period(text)
                masuda["length_of_text"] = util.get_length_of_text(text)
                masuda["distance_btw_commas"] = util.get_distance_btw_commas(text)
                masuda["kanji_content_rate"] = util.get_kanji_content_rate(text)
                masuda["sentiment_polarity_score"] = util.get_sentiment_polarity_score(text)
                result.append(masuda)
        with open("data/entry/masuda_{0}.json".format(i), "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
