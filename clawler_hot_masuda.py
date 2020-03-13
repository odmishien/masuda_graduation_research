import requests
from bs4 import BeautifulSoup
from masuda import Masuda
import json
import re

PAGE_FROM = 1
PAGE_TO = 344
BOOKMARK_PAGE_URL = "https://b.hatena.ne.jp/entrylist?url=https%3A%2F%2Fanond.hatelabo.jp%2F&sort=count&page={page}"


def get_hot_masuda_list(url):
    masuda_list = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    entry_list_unit = soup.find('section', 'entrylist-unit')

    # headerに1つだけエントリがあるのでそれを取得
    entry_list_header = entry_list_unit.find('div', 'entrylist-header')
    header_entry_list_contents = entry_list_header.find(
        'div', 'entrylist-contents')
    h_bookmark_count = get_bookmark_count(header_entry_list_contents)
    h_category = get_category(header_entry_list_contents)
    header_entry_url = header_entry_list_contents.find(
        'h3').find('a').get('href')
    h_title, h_content, h_masuda_id = get_masuda_title_and_content_and_id(
        header_entry_url)
    h_masuda = Masuda(h_masuda_id, h_title, h_content,
                      h_bookmark_count, h_category)
    masuda_list.append(h_masuda.__dict__)

    # それ以外のエントリを取得
    entry_list_item = entry_list_unit.find('ul', 'entrylist-item')
    entry_list_contents = entry_list_item.find_all(
        'div', 'entrylist-contents')
    for entry in entry_list_contents:
        bookmark_count = get_bookmark_count(entry)
        category = get_category(entry)
        entry_url = entry.find(
            'h3').find('a').get('href')
        title, content, masuda_id = get_masuda_title_and_content_and_id(
            entry_url)
        masuda = Masuda(masuda_id, title, content,
                        bookmark_count, category)
        masuda_list.append(masuda.__dict__)

    return masuda_list


def get_bookmark_count(entry_list_contents_obj):
    bookmark_a_tag = entry_list_contents_obj.find(
        'a', 'js-keyboard-entry-page-openable')
    return bookmark_a_tag.find('span').get_text()


def get_category(entry_list_contents_obj):
    category_li_tag = entry_list_contents_obj.find(
        'li', 'entrylist-contents-category')
    return category_li_tag.find('a').get_text()


def get_masuda_title_and_content_and_id(entry_url):
    res = requests.get(entry_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        section = soup.find('div', 'section')
        h3 = section.find('h3')
        # titleを取得
        title = h3.get_text().lstrip("■")

        # idを取得
        entry_url = h3.find('a').get('href')
        masuda_id = entry_url.lstrip("/")

        # contentを取得
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

        content = p.get_text()
        # content = re.sub(
        #     r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", content)  # URL文字列を削除
        # content = re.sub(r'[!-~]', "", content)  # 半角記号,数字,英字を削除
        # content = re.sub(r'[︰-＠]', "", content)  # 全角記号を削除
    except:
        title, content, masuda_id = None, None, None
    return title, content, masuda_id


if __name__ == '__main__':
    for i in range(PAGE_FROM, PAGE_TO):
        masuda_list = get_hot_masuda_list(BOOKMARK_PAGE_URL.format(page=i))
        with open('./data/hot_entry/masuda_{page}.json'.format(page=i), 'w') as f:
            json.dump(masuda_list, f, indent=2, ensure_ascii=False)
