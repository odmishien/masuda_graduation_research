from janome.tokenizer import Tokenizer
import re

t = Tokenizer()
index = 0
with open('masuda_hotentry.txt') as f:
    lines = f.readlines()
for line in lines:
    with open("./hot_jodoshi_entries/entry_" + str(index), "a") as f:
        line = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)","",line)
        line = re.sub(re.compile("[!-/:-@[-`{-~]"), '', line)
        line = re.sub(r'[1-9]', "", line)
        for token in t.tokenize(line):
            if token.part_of_speech.split(',')[0] == "助動詞":
                f.write("助動詞" + ' ')
            else:
                f.write(token.base_form + ' ')
    index += 1