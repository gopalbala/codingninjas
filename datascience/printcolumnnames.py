import csv

with open('year2017.csv') as inputFile:
    reader = csv.reader(inputFile)
    
    i = 0
    for row in reader:
        if i == 0:
            for j in range(len(row)):
                print(row[j])
            i+=1
        else:
            break 