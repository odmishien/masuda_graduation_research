from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle
import requests
from time import sleep
import json

masuda_list = []
clawl_zero_bookmark = True


def clawl(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    sections = soup.find_all('div', 'section')
    for section in sections:
        entry_url = section.find('a').get('href')
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
            text = p.get_text()
            masuda = {}
            masuda["id"] = entry_url
            masuda["text"] = text
            masuda["bookmark"] = bookmark_num
            masuda_list.append(masuda)


masuda_id = 1
for page in range(2, 1000):
    url = 'https://anond.hatelabo.jp/?mode=top&page=' + str(page)
    clawl(url)
with open('./data/masuda.json', 'w') as f:
    json.dump(masuda_list, f, indent=2, ensure_ascii=False)
