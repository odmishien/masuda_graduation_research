import sys
import numpy as np
import chainer
from chainer import serializers
import pickle
from config import Config
from MyNet import MyNet
from PIL import Image
import re

model = MyNet()
serializers.load_npz('models/mynet_final.model', model)

with open('masuda.pickle', 'rb') as f:
    data = pickle.load(f)
with open('masuda.txt', 'r') as f:
    lines = f.readlines()
test_images = []
for i in range(1, len(sys.argv)):
    image = sys.argv[i]
    img = np.array(Image.open('./resized_images/' + image),dtype="float32")
    dat = img.reshape((1, Config.MAX_WORDS_IN_TXT, Config.WORD_VEC_SIZE))
    print(dat.shape)
    img_index = int(re.sub(r'\D', '',image))
    line = lines[img_index]
    line = line.replace('\n','')
    y = model(dat[None, ...])
    print("pred:{}".format(y.data))
    print("truth:{}".format(data[line]))