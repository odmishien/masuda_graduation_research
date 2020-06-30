# import numpy as cuda.cupy
from chainer import optimizers, serializers, cuda, training, iterators
from chainer.training import extensions
import chainer.links as L
import chainer.functions as F
from config import Config
from MyNet import MyNet
from PIL import Image
import pickle
import os
import re

xp = cuda.cupy

images = os.listdir('./resized_images')
arrays_2 = [(re.search("[0-9]+", x).group(), x) for x in images]
arrays_2.sort(key=lambda x:(int(x[0])))
images = [x[1] for x in arrays_2]

arrays_list = []
for image in images:
    img = cuda.cupy.array(Image.open('./resized_images/' + image),dtype="float32")
    dat = img.reshape((1, Config.MAX_WORDS_IN_TXT, Config.WORD_VEC_SIZE))
    arrays_list.append(dat)
arrays_list = cuda.cupy.array(arrays_list)
print("text_making done.")

with open("masuda.pickle","rb") as f:
    masuda_dict = pickle.load(f)

bookmarks = []

with open("masuda.txt","r") as f:
    entries = f.readlines()
for entry in entries:
    entry = entry.replace('\n','')
    try:
        bookmark = masuda_dict[entry]
        bookmark = cuda.cupy.array([bookmark],dtype="float32")
        bookmarks.append(bookmark)
    except:
        bookmarks.append(cuda.cupy.array([0],dtype="float32"))
bookmarks = cuda.cupy.array(bookmarks,dtype="float32")
print("bookmarks_making done.")

# make tuple data list
data = []
for i in range(len(arrays_list)):
    t = (arrays_list[i], bookmarks[i])
    data.append(t)
print(data.size)
# make iterator
train_iter = iterators.SerialIterator(data, Config.BATCH_SIZE)

# make optimizer
model = L.Classifier(MyNet(),lossfun=F.mean_squared_error)
optimizer = optimizers.Adam()
optimizer.setup(model)

gpu_device = 0
cuda.get_device(gpu_device).use()
model.to_gpu(gpu_device)

updater = training.StandardUpdater(train_iter, optimizer)
trainer = training.Trainer(updater, (20, 'epoch'), out='result')
trainer.extend(extensions.LogReport())
trainer.extend(extensions.PrintReport( ["epoch", "main/loss", "validation/main/loss", "main/accuracy", "validation/main/accuracy", "elapsed_time"])) # エポック、学習損失、テスト損失、学習正解率、テスト正解率、経過時間
trainer.extend(extensions.ProgressBar()) # プログレスバー出力
trainer.run()

# for epoch in range(1000):
#     accum_loss = None
#     bs = Config.BATCH_SIZE
#     perm = cuda.cupy.random.permutation(num_train)
#     for i in range(0, num_train, bs):
#         x_sample = arrays_list[perm[i:(i + bs) if(i + bs < num_train) else num_train]]
#         y_sample = bookmarks[perm[i:(i + bs) if(i + bs < num_train) else num_train]]
#         model.zerograds()
#         loss = model.train(x_sample, y_sample)
#         loss.backward()
#         loss.unchain_backward()
#         optimizer.update()

#         accum_loss = loss.data if accum_loss is None else accum_loss + loss.data

#     print(epoch, accum_loss.data,flush=True)
#     if epoch % 100 == 0:
#         outfile = "models/mynet_{}.model".format(epoch)
#         serializers.save_cuda.cupyz(outfile, model)

outfile = "models/mynet_final.model"
serializers.save_npz(outfile, model)