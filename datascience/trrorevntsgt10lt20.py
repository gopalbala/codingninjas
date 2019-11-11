import numpy as np
import csv

reader = csv.DictReader(open('terrorismData.csv','r'),skipinitialspace=True)
l = list(reader)

cnt = 0
for row in l:
    if row['Day'] is not None and row['Day'] != '' and int(row['Day']) >= 10 and int(row['Day']) <=20:
        cnt+=1
print(cnt)

