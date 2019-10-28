import csv
with open('amazon_jobs_dataset.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    filedata = list(reader)
    
    locationwise = {}
    countbg = 0
    countsea = 0
    for row in filedata:
        if row['location'] != '':
            if 'Bangalore' in row['location']:
                countbg +=1
            elif 'Seattle' in row['location']:
                countsea +=1
    
    print(countbg,countsea)