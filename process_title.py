from util import is_include_bikkuri, is_include_dakeno, is_include_haikei, is_include_hiketsu, is_include_himitsu, is_include_houhou, is_include_housoku, is_include_kata, is_include_naze, is_include_odoroki, is_include_riyuu, is_include_shinzitsu, is_include_shirarezaru, is_include_special, is_include_sugo, is_include_sugoi, is_include_suteki, is_include_tokubetsu, is_include_totteoki, is_include_tukurikata, is_include_uragawa, is_include_zittai
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import japanize_matplotlib

is_list = ['is_include_bikkuri', 'is_include_dakeno', 'is_include_haikei', 'is_include_hiketsu', 'is_include_himitsu', 'is_include_houhou', 'is_include_housoku', 'is_include_kata', 'is_include_naze', 'is_include_odoroki', 'is_include_riyuu',
           'is_include_shinzitsu', 'is_include_shirarezaru', 'is_include_special', 'is_include_sugo', 'is_include_sugoi', 'is_include_suteki', 'is_include_tokubetsu', 'is_include_totteoki', 'is_include_tukurikata', 'is_include_uragawa', 'is_include_zittai']

df = pd.read_table('./data/for_bert/title_train.tsv',
                   names=('title', 'label'))
data = []
for i, row in df.iterrows():
    title = row['title']
    label = "Positive" if row['label'] else "Negative"
    data.append([label, is_include_bikkuri(
        title), is_include_dakeno(title), is_include_haikei(title), is_include_hiketsu(title), is_include_himitsu(title), is_include_houhou(title), is_include_housoku(title), is_include_kata(title), is_include_naze(title), is_include_odoroki(title), is_include_riyuu(title), is_include_shinzitsu(title), is_include_shirarezaru(title), is_include_special(title), is_include_sugo(title), is_include_sugoi(title), is_include_suteki(title), is_include_tokubetsu(title), is_include_totteoki(title), is_include_tukurikata(title), is_include_uragawa(title), is_include_zittai(title)])


plot_df = pd.DataFrame(data, columns=['label', 'is_include_bikkuri', 'is_include_dakeno', 'is_include_haikei', 'is_include_hiketsu', 'is_include_himitsu', 'is_include_houhou', 'is_include_housoku', 'is_include_kata', 'is_include_naze', 'is_include_odoroki', 'is_include_riyuu',
                                      'is_include_shinzitsu', 'is_include_shirarezaru', 'is_include_special', 'is_include_sugo', 'is_include_sugoi', 'is_include_suteki', 'is_include_tokubetsu', 'is_include_totteoki', 'is_include_tukurikata', 'is_include_uragawa', 'is_include_zittai'])

fig, axes = plt.subplots(5, 5)
row_index = 0
for i, is_content in enumerate(is_list):
    seaborn.countplot(
        data=plot_df, x=is_content, hue='label', ax=axes[i % 5, row_index])
    row_index = i // 5
plt.show()
