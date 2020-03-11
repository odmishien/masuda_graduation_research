import datetime
import matplotlib.pyplot as plt
import json

left = list(range(24))
bar_count = [0] * 24

for i in range(2, 5000):
    with open("data/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    for masuda in masuda_objs:
        try:
            masuda_datetime = datetime.datetime.strptime(
                masuda["id"], "%Y%m%d%H%M%S")
            h = masuda_datetime.hour
            bar_count[h] = bar_count[h] + 1
        except:
            pass

plt.bar(left, bar_count)
plt.show()
