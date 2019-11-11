import numpy as np
import csv

reader = csv.DictReader(open('terrorismData.csv'), skipinitialspace=True)
l = list(reader)

usl = []
killed = []
i = 0 
for row in l:
    if row['Country'] != '' and row['Country'] == 'United States':
        if row['Killed'] == '':
            print(0)
        else:
            print(int(float(row['Killed'])))
            i+=int(float(row['Killed']))
# print(i)
    # usl.append(row['Country'])
    # killed.append(row['Killed'])
    
# npusl = np.array(usl)
# npkilled = np.array(killed)

# npkilled[npkilled == ''] = '0.0'
# npkilled = np.array(npkilled, dtype=float)

# kius = np.where(npusl == 'United States')
# # print(kius)

# kcnt = npkilled[kius[0]]
# kc = kcnt[kcnt > 0]

# for i in kcnt:
#     print(int(i))

# print(len(kc))


