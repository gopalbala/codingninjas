import csv
with open('year2017.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    fileData = list(reader)
    
    monthwise = {}
    for row in fileData:
        if row['Month'] != '' and row['Killed'] != '':
            val = int(float(row['Killed']))
            if monthwise.get(row['Month']) != None:
                monthwise[row['Month']] = val + monthwise[row['Month']]
            else:
                monthwise[row['Month']] = val 
    for key in monthwise.keys():
        print(key,monthwise[key])