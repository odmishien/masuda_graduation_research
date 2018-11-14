import numpy as np
from chainer import optimizers, serializers, cuda
from config import Config
from MyNet import MyNet
import pickle
import os

arrays = os.listdir('./arrays')
arrays_list = []
for array in arrays:
    a = np.load("./arrays/" + array)
    arrays_list.append(a)
arrays_list = np.array(arrays_list)

print(arrays_list.shape)
print(arrays_list[0].shape)
quit()

with open("masuda.pickle","rb") as f:
    masuda_dict = pickle.load(f)

bookmarks = []

with open("masuda.txt","r") as f:
    entries = f.readlines()
for entry in entries:
    entry = entry.replace('\n','')
    try:
        bookmark = masuda_dict[entry]
        bookmarks.append(bookmark)
    except:
        bookmarks.append(0)
bookmarks = np.array(bookmarks)

model = MyNet()
optimizer = optimizers.Adam()
optimizer.setup(model)

#GPU設定
# gpu_device = 0
# cuda.get_device(gpu_device).use()
# model.to_gpu(gpu_device)

num_train = len(arrays_list)
for epoch in range(1000):
    accum_loss = None
    bs = Config.BATCH_SIZE
    perm = np.random.permutation(num_train)
    for i in range(0, num_train, bs):
        x_sample = arrays_list[perm[i:(i + bs) if(i + bs < num_train) else num_train]]
        y_sample = bookmarks[perm[i:(i + bs) if(i + bs < num_train) else num_train]]
        model.zerograds()
        loss = model.train(x_sample, y_sample)
        print(loss)
        loss.backward()
        loss.unchain_backward()
        optimizer.update()

        accum_loss = loss if accum_loss is None else accum_loss + loss

    print(epoch, accum_loss.data,flush=True)
    if epoch % 100 == 0:
        outfile = "models/mynet_{}.model".format(epoch)
        serializers.save_npz(outfile, model)

outfile = "models/mynet_final.model"
serializers.save_npz(outfile, model)