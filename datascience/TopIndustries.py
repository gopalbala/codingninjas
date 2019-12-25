# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
def checkSpell(String):
    word = String.split()[0]
    pos  = len(word)
    temp = word.replace('-','').lower()
    if temp == 'ecommerce':
        word = 'Ecommerce'
        return word
    return word+ String[pos:]
 
def str2int(string):
    return int(string.replace(',',''))
 
 
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
 
# Handle NaN and convert String to Number
df['IndustryVertical'].fillna('blank',inplace=True)
df['IndustryVertical'] = df['IndustryVertical'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
 
groupcols = df[df['IndustryVertical'] !='blank'].groupby(['IndustryVertical'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
total = groupcols.sum()
 
industry = []
fund     = []
for ind in groupcols.keys()[-1::-1][:5]:
    industry.append(ind)
    fund.append(groupcols[ind])
 
total =  sum(fund)
 
for i in range(len(industry)):
    print(industry[i],'%.2f'%(fund[i]/total*100))