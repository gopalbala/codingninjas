import csv

with open('year2017.csv') as inputFile:
    reader = csv.reader(inputFile)
    
    i = 0
    for row in reader:
        if i == 0:
            i+=1
            continue
        if i < 4:
            for j in range(len(row)):
                print(row[j], end = ' ') 
              
            i+=1
            print()
        else:
            break
        