import csv
with open('year2017.csv') as inputFile:
    reader = csv.reader(inputFile)
    fille_list = list(reader)

count = 0
i = 0
for row in fille_list:
    if i == 0:
        i+=1
        continue
    i+=1
    val = row[10]
    if row[3] != '' and row[3] == 'India':
        if val != '' and float(val) != 0:
            count += float(val)

print(int(count))