from janome.tokenizer import Tokenizer

t = Tokenizer()
index = 0
with open('masuda.txt') as f:
    lines = f.readlines()
for line in lines:
    with open('./entries/entry_'+str(index),'a') as f:
        for token in t.tokenize(line,wakati=True):
                f.write(token+' ')
    index += 1