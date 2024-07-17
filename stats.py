import csv
from jtop import jtop
import pandas as pd

def Merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1

run_once = 0
with jtop(interval = 0.5) as jetson:
	file_name = input("Enter file name: ") + ".csv"
	with open(file_name, 'w', newline='') as f:
		writer = csv.writer(f)
		while jetson.ok():
			my_dict = Merge(jetson.stats, jetson.power)
			w = csv.DictWriter(f, my_dict.keys())
			if (run_once == 0):
				w.writeheader()
				run_once = run_once + 1
			w.writerow(my_dict)


df = pd.read_csv(file_name)
print(df)
