import numpy as np
import csv
# from numpy import genfromtxt

# arr = genfromtxt('terrorismData.csv', delimiter=',',missing_values='',skip_header=1,filling_values='',quotechar = '"')

# arr = np.loadtxt(open("terrorismData.csv", "r"), delimiter=",", skiprows=1)

# arr = np.loadtxt(open("terrorismData.csv", "r"), delimiter=',',skiprows=1,dtype=str,ndmin=17)
#            dtype={'names': ('Year','Month','Day','Country','State','Region','City','Latitude','Longitude',
#                             'AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type'),
# ...                      'formats': ('S1', 'S1','S1','S1','S1','S1','S1','S1','S1','S1','S1','S1','S1','S1','S1','S1','S1')})

with open('terrorismData.csv','r') as dest_f:
    data_iter = csv.reader(dest_f,
                           delimiter = ',',
                           quotechar = '"')
    data = [data for data in data_iter]
    data_array = np.array(data)
    # print(data_array[:3])
    print(data_array)