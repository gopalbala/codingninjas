import pandas as pd
import numpy as np

df_year_fundings = pd.read_csv('startup_funding.csv')
yrfnd = {}



for i in df_year_fundings['Date']:
    yr = i[-4:]
    if yrfnd.get(yr):
        yrfnd[yr] = yrfnd[yr] + 1
    else:
        yrfnd[yr] = 1
                
l = []      
for i in yrfnd:
    l.append(i)
l.sort()
for i in l:
    print(i, yrfnd.get(i))
        