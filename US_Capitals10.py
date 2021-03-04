import csv
myObject = {}
with open("capital.csv") as f:
    for line in f.readlines():
        key, value = line.rstrip("\n").split(",")
        myObject[key] = value
sorted_dict = dict(sorted(myObject.items(), key=lambda item: item[1]))
first10pairs = {k: sorted_dict[k] for k in list(sorted_dict)[:10]}

w = csv.writer(open("US_SortedCapitals.txt", "w"))
for key, val in first10pairs.items():
    w.writerow([key, val])
