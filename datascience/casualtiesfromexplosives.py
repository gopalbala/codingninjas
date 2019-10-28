import csv
with open('year2017.csv') as inputFile:
    fileData = csv.DictReader(inputFile, skipinitialspace = True)

    count = 0
    i = 0    
    for row in fileData:
        if i == 0:
            i+=1
            continue
        
        if row['Weapon_type'] == 'Explosives' and row['casualities'] != '':
            count+=float(row['casualities'])
        
        i+=1
        
    print(int(count))