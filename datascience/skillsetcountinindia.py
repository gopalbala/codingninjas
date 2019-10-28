## Open and read data file as specified in the question
## Print the required output in given format
import csv
with open('amazon_jobs_dataset.csv') as inputFile:
    reader = csv.DictReader(inputFile, skipinitialspace = True)
    filedata = list(reader)
    skmap = {}
    skmap['Java'] = 0
    skmap['C++'] = 0
    skmap["Python"] = 0
    for row in filedata:
        if row['location'].startswith('IN'):
            if 'Bachelor' in row['BASIC QUALIFICATIONS'] or 'BS' in row['BASIC QUALIFICATIONS'] or 'BA' in row['BASIC QUALIFICATIONS']:
                if 'Java' in row['BASIC QUALIFICATIONS']:
                    skmap['Java'] = skmap['Java'] + 1
                if 'C++' in row['BASIC QUALIFICATIONS']:
                    skmap['C++'] = skmap['C++'] + 1
                if 'Python' in row['BASIC QUALIFICATIONS']:
                    skmap['Python'] = skmap['Python'] + 1
    curmax = skmap['Java']
    ma = 'Java'
    if skmap['C++'] > curmax:
        curmax = skmap['C++']
        ma = 'C++'
    elif skmap['Python'] > curmax:
        curmax = skmap['Python']
        ma = 'Python'
        
    for k in skmap.keys():
        print(k,skmap[k])