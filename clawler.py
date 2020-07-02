from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import re
import sys

clawl_zero_bookmark = False
clawl_hot_entry = True
hot_entry_standard_min = 100
hot_entry_standard_max = 200


def get_masuda_list(url):
    masuda_list = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    sections = soup.find_all('div', 'section')
    for section in sections:
        h3 = section.find('h3')
        keywords = h3.find_all('a', class_="keyword")
        for k in keywords:
            k.unwrap()

        entry_url = h3.find('a').get('href')
        p = section.find('p')
        try:
            p.find('p', 'share-button').extract()
            p.find('p', 'sectionfooter').extract()
        except:
            pass

        a_tags = p.find_all('a')
        for a_tag in a_tags:
            a_tag.unwrap()

        other_p_tags = p.find_all('p')
        for other_p in other_p_tags:
            other_p.unwrap()

        try:
            with urlopen('http://b.hatena.ne.jp/entry/s/anond.hatelabo.jp' + str(entry_url)) as bookmark_url:
                bookmark_page = BeautifulSoup(bookmark_url, 'html.parser')
                bookmark_num = int(bookmark_page.find(
                    'span', 'entry-info-users').find('span').get_text())
        except:
            bookmark_num = 0

        if not clawl_zero_bookmark and bookmark_num == 0:
            pass
        else:
            if clawl_hot_entry:
                if bookmark_num > hot_entry_standard_min & bookmark_num < hot_entry_standard_max:
                    title = h3.get_text().lstrip("■")
                    text = p.get_text()
                    # text = re.sub(
                    #     r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)  # URL文字列
                    # text = re.sub(r'[!-~]', "", text)  # 半角記号,数字,英字
                    # text = re.sub(r'[︰-＠]', "", text)  # 全角記号
                    masuda_id = entry_url.lstrip("/")
                    masuda = {}
                    masuda["masuda_id"] = masuda_id
                    masuda["title"] = title
                    masuda["content"] = text
                    masuda["bookmark_count"] = bookmark_num
                    masuda["category"] = None
                    masuda_list.append(masuda)
            else:
                title = h3.get_text().lstrip("■")
                text = p.get_text()
                # text = re.sub(
                #     r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)  # URL文字列
                # text = re.sub(r'[!-~]', "", text)  # 半角記号,数字,英字
                # text = re.sub(r'[︰-＠]', "", text)  # 全角記号
                masuda_id = entry_url.lstrip("/")
                masuda = {}
                masuda["masuda_id"] = masuda_id
                masuda["title"] = title
                masuda["content"] = text
                masuda["bookmark_count"] = bookmark_num
                masuda["category"] = None
                masuda_list.append(masuda)
    return masuda_list


def dump_list_to_json(masuda_list, page):
    data_path = "./data/entry"
    if clawl_hot_entry:
        data_path = "./data/hot_entry"
    if len(masuda_list > 0):
        with open('{data_path}/masuda_{page}.json'.format(data_path=data_path, page=page), 'w') as f:
            json.dump(masuda_list, f, indent=2, ensure_ascii=False)


args = sys.argv
page_from = int(args[1])
page_to = int(args[2])
for page in range(page_from, page_to, -1):
    url = 'https://anond.hatelabo.jp/?mode=top&page=' + str(page)
    masuda_list = get_masuda_list(url)
    dump_list_to_json(masuda_list, page)
