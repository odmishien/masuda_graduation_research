import re
import regex

def get_num_of_sentences(text):
    split_text = re.split('[。！？!?]', text)
    return len(split_text) - 1

def get_num_of_comma(text):
    return text.count('、')

def get_num_of_period(text):
    return text.count('。')

def get_length_of_text(text):
    return len(text)

# 読点間距離
# 文の長さ - 読点数 - 1 / 読点数 + 1
def get_distance_btw_commas(text):
    length_of_text = get_length_of_text(text)
    num_of_comma = get_num_of_comma(text)
    return float(length_of_text - num_of_comma - 1) / (num_of_comma + 1)

# 漢字含有率
# 文章中の漢字の総数 / 文章中の漢字と仮名の総数
def get_kanji_content_rate(text):
    kanji_list = regex.findall(r'\p{Han}', text)
    hiragana_list = regex.findall(r'\p{Hiragana}', text)
    katakana_list = regex.findall(r'\p{Katakana}', text)
    # このままだと単語がリストに入っているのでその長さを数える
    kanji_count, kana_count = 0, 0
    for kanji in kanji_list:
        kanji_count += len(kanji)
    for hiragana in hiragana_list:
        kana_count += len(hiragana)
    for katakana in katakana_list:
        kana_count += len(katakana)
    return float(kanji_count) / (kanji_count + kana_count)
