## Open and read data file as specified in the question
## Print the required output in given format
## Open and read data file as specified in the question
## Print the required output in given format
## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
import csv
with open('terrorismData.csv') as file_obj:
    file_data = csv.DictReader(file_obj,skipinitialspace=True)
   
    day = []
   
    for row in file_data:
        if row['Day'] != '' and row['Day'] != '0':
            day.append(row['Day'])
   
    np_day      = np.array(day)
    np_day_u, np_day_count = np.unique(np_day, return_counts=True)
    ind = np_day_count.argmax()
    print(np_day_u[ind], np_day_count[ind])
   
    