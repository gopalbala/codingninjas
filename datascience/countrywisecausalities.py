import csv
with open('year2017.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    fileData = list(reader)
    
    countrywise = {}
    for row in fileData:
        if row['Country'] != '':
            val = 0
            if row['casualities'] != '':
                val = int(float(row['casualities']))
            if countrywise.get(row['Country']) != None:
                countrywise[row['Country']] = val + countrywise[row['Country']]
            else:
                countrywise[row['Country']] = val 
    for key in countrywise.keys():
        print(key,countrywise[key])