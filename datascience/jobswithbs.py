import csv
with open('amazon_jobs_dataset.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    filedata = list(reader)
    bcount = 0
    for row in filedata:
        if 'Bachelor' in row['BASIC QUALIFICATIONS'] or 'BS' in row['BASIC QUALIFICATIONS'] or 'BA' in row['BASIC QUALIFICATIONS']:
            bcount+=1
    print(bcount)