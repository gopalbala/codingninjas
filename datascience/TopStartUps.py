# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
def checkSpell(String):
    newStr = String.replace(' ','').lower()
    if newStr == 'ola' or newStr == 'olacabs':
        String = 'Ola'
    elif newStr == 'flipkart' or newStr == 'flipkart.com':
        String = 'Flipkart'
    elif newStr == 'oyo' or newStr == 'oyorooms' or newStr=='oyoroom' or newStr=='oyofit':
        String = 'Oyo'
    elif newStr == 'paytm' or newStr == 'paytmmarketplace':
        String = 'Paytm'
    return String
    
    
def str2int(string):
    return int(string.replace(',',''))
 
 
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
 
# Handle NaN and convert String to Number
df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
 
groupcols = df[df['StartupName'] !='blank'].groupby(['StartupName'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()
 
for startup in groupcols.keys()[-1::-1][:5]:
    print(startup)
 