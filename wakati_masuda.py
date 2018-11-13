from janome.tokenizer import Tokenizer

t = Tokenizer()

with open('masuda.txt') as f:
    lines = f.readlines()
with open('wakati_masuda.txt','a') as f:
    for line in lines:
        for token in t.tokenize(line,wakati=True):
            f.write(token+' ')