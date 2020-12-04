import os
import json
import util
from tqdm import tqdm

# for i in tqdm(range(1, 4995)):
#     if os.path.exists("data/hot_entry/masuda_{0}.json".format(i)):
#         with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
#             hot_masuda_objs = json.load(f)
#         result = []
#         for masuda in hot_masuda_objs:
#             text = masuda["content"]
#             if text is not None:
#                 masuda["num_of_sentences"] = util.get_num_of_sentences(text)
#                 masuda["num_of_comma"] = util.get_num_of_comma(text)
#                 masuda["num_of_period"] = util.get_num_of_period(text)
#                 masuda["length_of_text"] = util.get_length_of_text(text)
#                 masuda["distance_btw_commas"] = util.get_distance_btw_commas(text)
#                 masuda["kanji_content_rate"] = util.get_kanji_content_rate(text)
#                 masuda["sentiment_polarity_score"] = util.get_sentiment_polarity_score(text)
#                 masuda["raising_discussion_score"] = util.get_raising_discussion_score(masuda["masuda_id"], int(masuda["bookmark_count"]))
#                 masuda["num_of_exclamation_mark"] = util.get_num_of_exclamation_mark(text)
#                 masuda["num_of_question_mark"] = util.get_num_of_question_mark(text)
#                 masuda["is_include_bikkuri"] = util.is_include_bikkuri(text)
#                 masuda["is_include_dakeno"] = util.is_include_dakeno(text)
#                 masuda["is_include_haikei"] = util.is_include_haikei(text)
#                 masuda["is_include_hiketsu"] = util.is_include_hiketsu(text)
#                 masuda["is_include_himitsu"] = util.is_include_himitsu(text)
#                 masuda["is_include_houhou"] = util.is_include_houhou(text)
#                 masuda["is_include_housoku"] = util.is_include_housoku(text)
#                 masuda["is_include_naze"] = util.is_include_naze(text)
#                 masuda["is_include_odoroki"] = util.is_include_odoroki(text)
#                 masuda["is_include_riyuu"] = util.is_include_riyuu(text)
#                 masuda["is_include_shinzitsu"] = util.is_include_shinzitsu(text)
#                 masuda["is_include_shirarezaru"] = util.is_include_shirarezaru(text)
#                 masuda["is_include_special"] = util.is_include_special(text)
#                 masuda["is_include_sugo"] = util.is_include_sugo(text)
#                 masuda["is_include_sugoi"] = util.is_include_sugoi(text)
#                 masuda["is_include_suteki"] = util.is_include_suteki(text)
#                 masuda["is_include_tokubetsu"] = util.is_include_tokubetsu(text)
#                 masuda["is_include_totteoki"] = util.is_include_totteoki(text)
#                 masuda["is_include_tukurikata"] = util.is_include_tukurikata(text)
#                 masuda["is_include_uragawa"] = util.is_include_uragawa(text)
#                 masuda["is_include_zittai"] = util.is_include_zittai(text)
#             result.append(masuda)
#         with open("data/hot_entry/masuda_{0}.json".format(i), "w") as f:
#             json.dump(result, f, indent=2, ensure_ascii=False)

for i in tqdm(range(6659, 8000)):
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
                masuda["distance_btw_commas"] = util.get_distance_btw_commas(
                    text)
                masuda["kanji_content_rate"] = util.get_kanji_content_rate(
                    text)
                # masuda["sentiment_polarity_score"] = util.get_sentiment_polarity_score(
                #     text)
                masuda["raising_discussion_score"] = util.get_raising_discussion_score(
                    masuda["masuda_id"], int(masuda["bookmark_count"]))
                masuda["num_of_exclamation_mark"] = util.get_num_of_exclamation_mark(
                    text)
                masuda["num_of_question_mark"] = util.get_num_of_question_mark(
                    text)
                masuda["is_include_bikkuri"] = util.is_include_bikkuri(text)
                masuda["is_include_dakeno"] = util.is_include_dakeno(text)
                masuda["is_include_haikei"] = util.is_include_haikei(text)
                masuda["is_include_hiketsu"] = util.is_include_hiketsu(text)
                masuda["is_include_himitsu"] = util.is_include_himitsu(text)
                masuda["is_include_houhou"] = util.is_include_houhou(text)
                masuda["is_include_housoku"] = util.is_include_housoku(text)
                masuda["is_include_naze"] = util.is_include_naze(text)
                masuda["is_include_odoroki"] = util.is_include_odoroki(text)
                masuda["is_include_riyuu"] = util.is_include_riyuu(text)
                masuda["is_include_shinzitsu"] = util.is_include_shinzitsu(
                    text)
                masuda["is_include_shirarezaru"] = util.is_include_shirarezaru(
                    text)
                masuda["is_include_special"] = util.is_include_special(text)
                masuda["is_include_sugo"] = util.is_include_sugo(text)
                masuda["is_include_sugoi"] = util.is_include_sugoi(text)
                masuda["is_include_suteki"] = util.is_include_suteki(text)
                masuda["is_include_tokubetsu"] = util.is_include_tokubetsu(
                    text)
                masuda["is_include_totteoki"] = util.is_include_totteoki(text)
                masuda["is_include_tukurikata"] = util.is_include_tukurikata(
                    text)
                masuda["is_include_uragawa"] = util.is_include_uragawa(text)
                masuda["is_include_zittai"] = util.is_include_zittai(text)
            result.append(masuda)
        with open("data/entry/masuda_{0}.json".format(i), "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
