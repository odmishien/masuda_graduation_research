import pickle
with open('masuda.pickle','rb') as p:
    masuda = pickle.load(p)
with open('masuda.txt','w') as f:
    for key in masuda.keys():
        f.write(key+'\n')
