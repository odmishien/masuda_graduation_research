import pickle
with open('masuda.pickle','rb') as p:
    masuda = pickle.load(p)
print(masuda.values())