import csv
with open('amazon_jobs_dataset.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    filedata = list(reader)
    cmap = {}
    for row in filedata:
        countrycode = row['location'][0:2]
        if 'Java' in row['BASIC QUALIFICATIONS']:
            if cmap.get(countrycode) != None:
                cmap[countrycode] = cmap[countrycode] + 1
            else:
                cmap[countrycode] = 1
    mc = ''
    mv = 0
    for k in cmap:
        if cmap[k] > mv:
            mv = cmap[k]
            mc = k
    
    print(mc,mv)