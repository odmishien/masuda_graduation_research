import matplotlib.pyplot as plt
import japanize_matplotlib
import json

content_length = []
bookmark_count = []

for i in range(1, 344):
    with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    for masuda in masuda_objs:
        if masuda["content"] is not None:
            content_length.append(len(masuda["content"]))
            bookmark_count.append(int(masuda["bookmark_count"]))

plt.scatter(bookmark_count, content_length)
plt.show()
