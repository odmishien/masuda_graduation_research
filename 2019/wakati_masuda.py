from janome.tokenizer import Tokenizer
import re
import unicodedata
import string

t = Tokenizer()

with open('masuda.txt') as f:
    lines = f.readlines()
with open('wakati_masuda_hot_joshi.txt','w') as f:
    for line in lines:
        line = unicodedata.normalize("NFKC", line)
        table = str.maketrans("", "", string.punctuation  + "「」、。・")
        line = line.translate(table)
        line = re.sub(r"(https?|http)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)","",line)
        line = re.sub(re.compile("[!-/:-@[-`{-~]"), '', line)
        line = re.sub(r'\d*', "", line)
        for token in t.tokenize(line):
            part_of_speech = token.part_of_speech.split(',')[0]
            if part_of_speech == "助詞":
                f.write("助詞" + ' ')
            else:
                f.write(token.base_form + ' ')