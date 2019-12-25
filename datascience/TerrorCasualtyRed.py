import numpy as np
import csv
with open('terrorismData.csv') as file_obj:
    file_data = csv.DictReader(file_obj,skipinitialspace=True)
   
    state = []
    killed = []
    wounded = []
   
    for row in file_data:
        if row['Country'] == 'India':
            state.append(row['State'])
            killed.append(row['Killed'])
            wounded.append(row['Wounded'])
          
    np_state   = np.array(state)
    np_killed  = np.array(killed)
    np_wounded = np.array(wounded)   
    
    np_killed[np_killed == ''] = '0.0'
    np_wounded[np_wounded == ''] = '0.0'
       
    np_killed  = np.array(np_killed,dtype=float)
    np_killed  = np.array(np_killed,dtype=int)
    np_wounded = np.array(np_wounded,dtype=float)
    np_wounded = np.array(np_wounded,dtype=int)
    np_casualty = np_killed + np_wounded
    
    bool_red = (np_state == 'Jharkhand') | (np_state == 'Odisha') | (np_state == 'Andhra Pradesh') | (np_state == 'Chhattisgarh')
    bool_jk = (np_state == 'Jammu and Kashmir')
    
    np_cas_filter  = np_casualty[(bool_red)]
    np_jk_filter = np_casualty[(bool_jk)]
    
    cas_count = np.sum(np_cas_filter)
    cas_jk = np.sum(np_jk_filter)
    
    print(cas_count, cas_jk)
   