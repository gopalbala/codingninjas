import csv
with open('amazon_jobs_dataset.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    filedata = list(reader)
    cancount = 0
    for row in filedata:
        if row['location'] != '' and row['location'].startswith('CA'):
            cancount+=1
    print(cancount)