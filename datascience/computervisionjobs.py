import csv
with open('amazon_jobs_dataset.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    filedata = list(reader)
    cvcount = 0
    for row in filedata:
        if 'Computer Vision' in row['BASIC QUALIFICATIONS']:
            cvcount+=1
    print(cvcount)