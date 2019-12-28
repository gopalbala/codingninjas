# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
def checkSpell(String):
    outStr = ''
    char ='a'
    prevchar = ''
   
    for char in String:
        if prevchar != ' ':
            if char.isupper():
                outStr = outStr + ' ' + char
            else:
                outStr = outStr + char   
        else:
            outStr = outStr + char
        prevchar = char
    return outStr.strip().title()
 
def str2int(string):
    return int(string.replace(',',''))
 
 
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
 
# Handle NaN and convert String to Number
df.InvestmentType.fillna('blank',inplace=True)
df.InvestmentType = df.InvestmentType.apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
 
groupcols = df[df.InvestmentType !='Blank'].groupby(['InvestmentType'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
total = groupcols.sum()
 
plt.axis("equal")
plt.pie(groupcols,labels=groupcols.keys(),autopct='%.2f%%')
plt.show()
 
for i in range(len(groupcols)-1,-1,-1):
    print(groupcols.keys()[i],'%.2f'%(groupcols[i]/total*100))