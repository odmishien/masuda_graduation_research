import os
import pickle
import re

import chainer.functions as F
import chainer.links as L
import numpy as np
from chainer import Variable, iterators
from gensim.models import word2vec

bs = 100

x_list = []

model = word2vec.Word2Vec.load("masuda.model_20181213")
with open('./pickle/masuda_hotentry','rb') as p:
    masuda = pickle.load(p)
# エントリーをベクトルに変換する
entries = os.listdir("./meishi_entries")
arrays_2 = [(re.search("[0-9]+", x).group(), x) for x in entries]
arrays_2.sort(key=lambda x:(int(x[0])))
entries = [x[1] for x in arrays_2]

delete_entries = []
for entry in entries:
    with open('./meishi_entries/'+ entry,"r") as f:
        line = f.readline()
        words = line.rstrip().split(' ')
    x = []
    for word in words:
        try:
            vec = model.wv[word]
            x.append(vec)
        except:
            print(word)
    if len(x) > 0:
        x_list.append(x)
    else:
        delete_entries.append(entry)
x_data = [np.array(x, dtype=np.float32) for x in x_list]

keys = []
for e in entries:
    if not e in delete_entries:
        with open ('./hotentries/' + e, "r") as f:
            line = f.readline()
        words = line.rstrip().split(' ')
        keys.append(words)
# teaching
y_list = []
for key in keys:
    key = ''.join(key)
    try:
        bookmark = masuda[key]
        y_list.append(bookmark)
    except:
        print("no key")
y_data = [np.array([y], dtype=np.float32) for y in y_list]
# Word Embeddings (Word2Vec)
# n_vocab = 500
emb_dim = 100
# word_embed = L.EmbedID(n_vocab, emb_dim, ignore_label=-1)

# LSTM
use_dropout = 0.25
in_size = emb_dim
n_lstm_layers = 2
n_lstm_hidden = 200
calc_lstm = L.NStepLSTM(n_layers=n_lstm_layers, in_size=in_size, out_size=n_lstm_hidden, dropout=use_dropout)

# make optimizer
model = L.Classifier(MyNet(),lossfun=F.mean_squared_error)
optimizer = optimizers.Adam()
optimizer.setup(model)

# make iterator
data = []
for i in range(len(x_data)):
    t = (x_data[i], y_data[i])
    data.append(t)
train_iter = iterators.SerialIterator(data,bs)

# Output
n_output = 1
calc_output = L.Linear(in_size=n_lstm_hidden, out_size=n_output)

hx = None
cx = None

x_inp = []
for x in x_data:
    xi = F.dropout(x, ratio=use_dropout)
    x_inp.append(xi)

for x in x_inp:
    print(x.shape)

hy, cy, oy = calc_lstm(hx=hx, cx=cx, xs=x_inp)
output = []
for y in oy:
    o = calc_output(y)
    print(o.shape)
    output.append(o)

loss = []
for y, y_hat in zip(output, y_data):
    print(y.shape, y_hat.shape)
    loss.append(F.mean_squared_error(y[-1], y_hat))
