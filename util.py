import re
import regex
import oseti
import requests
from bs4 import BeautifulSoup

# 1次元のリストにある数値を0-1に正規化する
def min_max(l):
    l_min = min(l)
    l_max = max(l)
    return [(i - l_min) / (l_max - l_min) for i in l]

def get_num_of_sentences(text):
    split_text = re.split('[。！？!?]', text)
    return len(split_text) - 1

def get_num_of_comma(text):
    return text.count('、')

def get_num_of_period(text):
    return text.count('。')

def get_num_of_exclamation_mark(text):
    return text.count('!') + text.count('！')

def get_num_of_question_mark(text):
    return text.count('?') + text.count('？')

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
    if kanji_count == 0:
        return 0
    return float(kanji_count) / (kanji_count + kana_count)

# 評価極性スコア
# osetiを使う
def get_sentiment_polarity_score(text):
    analyzer = oseti.Analyzer()
    score = analyzer.analyze(text)
    if (len(score) > 0):
        return sum(score) / len(score)
    else:
        return 0

def get_raising_discussion_score(masuda_id, bookmark_count):
    if bookmark_count == 0:
        return 0
    url = "https://b.hatena.ne.jp/entry/s/anond.hatelabo.jp/{masuda_id}".format(masuda_id=masuda_id)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    if soup.find('span','entry-info-comment'):
        comment_count = int(soup.find('span','entry-info-comment').find('span').get_text())
        if comment_count != 0:
            return comment_count / bookmark_count
        else:
            return 0
    else:
        return 0

def get_unique_elements_btw_list(a, b):
    return list(set(a) - set(b))

def is_include_haikei(text):
    return 1 if '背景' in text else 0

def is_include_riyuu(text):
    return 1 if '理由' in text else 0

def is_include_himitsu(text):
    return 1 if '秘密' in text else 0

def is_include_naze(text):
    return 1 if 'なぜ' in text else 0

def is_include_uragawa(text):
    return 1 if '裏側' in text else 0

def is_include_shinzitsu(text):
    return 1 if '真実' in text else 0

def is_include_shirarezaru(text):
    return 1 if '知られざる' in text else 0

def is_include_zittai(text):
    return 1 if '実態' in text else 0

def is_include_housoku(text):
    return 1 if '法則' in text else 0

def is_include_tukurikata(text):
    return 1 if '作り方' in text else 0

def is_include_houhou(text):
    return 1 if '方法' in text else 0

def is_include_hiketsu(text):
    return 1 if '秘訣' in text else 0

def is_include_sugoi(text):
    return 1 if 'すごい' in text else 0

def is_include_sugo(text):
    return 1 if '凄' in text else 0

def is_include_odoroki(text):
    return 1 if '驚き' in text else 0

def is_include_suteki(text):
    return 1 if '素敵' in text else 0

def is_include_bikkuri(text):
    return 1 if 'びっくり' in text else 0

def is_include_tokubetsu(text):
    return 1 if '特別' in text else 0

def is_include_special(text):
    return 1 if 'スペシャル' in text else 0

def is_include_totteoki(text):
    return 1 if 'とっておき' in text else 0

def is_include_dakeno(text):
    return 1 if 'だけの' in text else 0
