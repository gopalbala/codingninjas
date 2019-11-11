## Open and read data file as specified in the question
## Print the required output in given format
## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
import csv

reader = csv.DictReader(open('terrorismData.csv'), skipinitialspace=True)
l = list(reader)

usl = []
killed = []
for row in l:
    usl.append(row['Country'])
    killed.append(row['Killed'])

npusl = np.array(usl)
npkilled = np.array(killed)

npkilled[npkilled == ''] = '0.0'
npkilled = np.array(npkilled, dtype=float)
bus = npusl == 'United States'
kcnt = npkilled[bus]
print(int(np.sum(kcnt)))

