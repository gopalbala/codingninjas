import csv

with open('year2017.csv') as inputFile:
    reader = csv.reader(inputFile)
    
    i = 0
    for row in reader:
        if i == 0:
            i+=1
            continue
        if i < 11:
            print(row[3])
            i+=1
        else:
            break