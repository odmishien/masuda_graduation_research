import datetime
import matplotlib.pyplot as plt
import json

left = list(range(24))
bar_count = [0] * 24

for i in range(1, 344):
    with open("data/hot_entry/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    for masuda in masuda_objs:
        if masuda["masuda_id"] is not None:
            try:
                masuda_datetime = datetime.datetime.strptime(
                    masuda["masuda_id"], "%Y%m%d%H%M%S")
                h = masuda_datetime.hour
                bar_count[h] = bar_count[h] + 1
            except:
                pass

plt.bar(left, bar_count)
plt.show()
