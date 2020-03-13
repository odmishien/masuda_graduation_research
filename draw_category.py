import matplotlib.pyplot as plt
import japanize_matplotlib
import json

category_to_count = {}

for i in range(1, 344):
    with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    for masuda in masuda_objs:
        category = masuda["category"]
        if category in category_to_count.keys():
            category_to_count[category] += 1
        else:
            category_to_count[category] = 1

categories = category_to_count.keys()
counts = []
for category in categories:
    counts.append(category_to_count[category])

plt.bar(categories, counts)
plt.show()
