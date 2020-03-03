from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle
import requests
from time import sleep
import json
import sys

clawl_zero_bookmark = True

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
            title = h3.get_text().lstrip("■")
            text = p.get_text()
            masuda_id = entry_url.lstrip("/")
            masuda = {}
            masuda["title"] = title
            masuda["id"] = masuda_id
            masuda["text"] = text
            masuda["bookmark"] = bookmark_num
            masuda_list.append(masuda)
    return masuda_list

def dump_list_to_json(list, page):
    with open('./data/masuda_{page}.json'.format(page=page), 'w') as f:
        json.dump(masuda_list, f, indent=2, ensure_ascii=False)

args = sys.argv
page_from = int(args[1])
page_to = int(args[2])
for page in range(page_from, page_to, -1):
    url = 'https://anond.hatelabo.jp/?mode=top&page=' + str(page)
    masuda_list = get_masuda_list(url)
    dump_list_to_json(masuda_list, page)
