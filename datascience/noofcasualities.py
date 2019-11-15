import numpy as np
import csv

killed = []
wounded = []
casual = []
grp = []
city = []
with open('terrorismData.csv',encoding='ISO-8859-1') as data:
    reader = csv.DictReader(data)
    for row in reader:
        if row['Year'] is not None and row['Year'] != '' and int(row['Year']) == 1999:
            if row['Month'] is not None and row['Month'] != '' and int(row['Month']) >=5 and int(row['Month']) <= 7:
                ck = 0
                cw = 0
                if row["Killed"] == '':
                    ck = 0
                    killed.append(0)
                else:
                    ck = int(float(row['Killed']))
                    killed.append(ck)
                if row["Wounded"] == '':
                    cw = 0
                    wounded.append(0)
                else:
                    cw = int(float(row['Wounded']))
                    wounded.append(cw)
                casual.append(ck + cw)
                city.append(row['City'])
                grp.append(row['Group'])
                
    npcasual = np.array(casual)
    npgrp = np.array(grp)
    npcity = np.array(city)
    maxidx = np.argmax(casual)
    print(npcasual[maxidx],npcity[maxidx],npgrp[maxidx])
    