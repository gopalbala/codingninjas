import pandas as pd

import numpy as np

df_terrorism=pd.read_csv('terrorismData.csv')

year=len(set(df_terrorism['Year']))

df_terrorism=df_terrorism[df_terrorism['Country']=='India']

df_terrorism['Casualty']=df_terrorism['Killed']+df_terrorism['Wounded']

Jammu_state=df_terrorism[df_terrorism['State']=='Jammu and Kashmir']

red_state=df_terrorism[(df_terrorism['State']=='Jharkhand')|(df_terrorism['State']=='Odisha')|(df_terrorism['State']=='Andhra Pradesh')|(df_terrorism['State']=='Chhattisgarh')]

red_casualty=int(np.sum(red_state['Casualty']))

Jammu_casualty=int(np.sum(Jammu_state['Casualty']))

print(red_casualty//year,Jammu_casualty//year)