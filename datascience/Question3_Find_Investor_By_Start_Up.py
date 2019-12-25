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


# Handle NaN and convert String to Number 
def getInvestor(investor):
    parse = [',','&',' and ','\xa0','.']
    inp = [investor]
    for spchar in parse: 
        out = []
        while len(inp) > 0: 
            inStr = str(inp.pop())          
            arr1 = inStr.split(spchar)
            out.extend(arr1)
        inp = out 
    
    return inp

def resolveInvestor(investor):

    if investor.lower() == 'accel' or 'accel ' in investor.lower(): 
        return 'Accel Partners'
    
    if investor.lower() == 'indian angels network' or investor.lower() == 'indian angel network (ian)': 
        return 'Indian Angel Network'
    
    if 'sequoia' in investor.lower(): 
        return 'Sequoia Capital'
    
    if 'kalaari' in investor.lower(): 
        return 'Kalaari Capital'
    
    if 'blume' in investor.lower():
        return 'Blume Ventures'
    
    if 'saif' in investor.lower(): 
        return 'SAIF Partners'
    
    return investor 

data = pd.read_csv('startup_funding.csv')
df   = data.copy()

df['StartupName'].fillna('blank',inplace=True)
df['StartupName'] = df['StartupName'].apply(checkSpell)

df.InvestorsName.fillna('blank',inplace=True)
df = df[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

## As the investors column has multiple investors, we are exploding it into multiple records.  
## For example, if one Startup has three investors it will be exploded into three rows. 
investors = []
for i in range(len(df.InvestorsName)): 
    investor = df.iloc[i]['InvestorsName']
    startUp  = df.iloc[i]['StartupName']
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append([ele.strip().title(), startUp])
inv_st_df = pd.DataFrame(investors,columns=['InvestorsName', 'StartUp'])
            
## Grouping the records by InvestorsName and Start Up to get the Unique List of Start UPs invested by 
## an Investor           
groupcols = inv_st_df.groupby(['InvestorsName','StartUp']).count()
df1 = pd.DataFrame(groupcols.reset_index())
freq = df1.InvestorsName.value_counts()

for investor in freq.keys()[:5]:
    print(investor,freq[investor])
