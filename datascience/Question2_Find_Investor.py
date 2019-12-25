# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

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

df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]

investors = []
for investor in df.InvestorsName: 
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip())
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other': 
            investors.append(ele.strip().title())

inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])

