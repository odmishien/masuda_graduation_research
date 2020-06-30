from urllib.request import urlopen
from bs4 import BeautifulSoup

dic = {}
url = urlopen(str(input("増田エントリのURLを入力してください：")))
soup = BeautifulSoup(url,'html.parser')
# print(soup.prettify())
sections = soup.find_all('div','section')
for section in sections:
    entry_url = section.find('a').get('href')
    p = section.find('p')
    try:
        p.find('p','share-button').extract()
        p.find('p','sectionfooter').extract()
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
            bookmark_num = int(bookmark_page.find('span','entry-info-users').find('span').get_text())
    except:
        bookmark_num = 0

    text = p.get_text()
    dic['text'] = text
    dic['bookmark'] = bookmark_num

from janome.tokenizer import Tokenizer

t = Tokenizer()
with open('masuda_from_url.txt','w') as f:
    sentence = dic['text']
    print(sentence)
    for token in t.tokenize(sentence[0],wakati=True):
        f.write(token+' ')

from gensim.models import word2vec
import numpy as np

new_max = 255
new_min = 0
old_max = 9.400702
old_min = -10.083586
max_height = 4168

model = word2vec.Word2Vec.load("masuda.model_2")
vocab = model.wv.vocab
with open("masuda_from_url.txt") as f:
    words = f.read()
words = words.split()
nd_array = np.zeros((max_height, 100), dtype=np.float32)
for i, w in enumerate(words):
    old_val = model[w]
    new_val = (new_max - new_min) * (old_val - old_min) / (old_max - old_min) + new_min
    nd_array[i] = new_val

from PIL import Image

image = Image.fromarray(np.uint8(nd_array))
image = image.resize((100,100))

from chainer import serializers
from config import Config
from MyNet import MyNet

model = MyNet()
serializers.load_npz('models/mynet_final.model', model)

img = np.array(image,dtype="float32")
dat = img.reshape((1, Config.MAX_WORDS_IN_TXT, Config.WORD_VEC_SIZE))
y = model(dat[None, ...])

print(dic['text'])
print("pred:{}".format(y.data))
print("truth:{}".format(dic['bookmark']))