import pickle
with open('./pickle/masuda_hotentry','rb') as p:
    masuda = pickle.load(p)
with open('masuda_hotentry.txt','a') as f:
    for key in masuda.keys():
        f.write(key+'\n')
