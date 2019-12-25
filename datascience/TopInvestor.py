# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
def getInvestorMap():
    dict_arr  = []
    dict_arr.append(("Accel Partner","Accel Partners"))
    dict_arr.append(("Accel Partners India","Accel Partners"))
    dict_arr.append(("Accel India","Accel Partners"))
    dict_arr.append(("Accel US","Accel Partners"))
    dict_arr.append(("Accel","Accel Partners"))
    dict_arr.append(("Accel Partners RNT Associates","Accel Partners"))
    #dict_arr.append(("Blume ventures","Blume Ventures"))
    dict_arr.append(("Sequoia Capital India","Sequoia Capital"))
    dict_arr.append(("Sequoia Capital Global Equities","Sequoia Capital"))
    dict_arr.append(("Sequoia India","Sequoia Capital"))
    dict_arr.append(("Sequoia","Sequoia Capital"))
    dict_arr.append(("Kalaari Capital Partners","Kalaari Capital"))
    dict_arr.append(("Kalaari Capital Accelerator Program","Kalaari Capital"))
    dict_arr.append(("Indian Angels Network","Indian Angel Network"))
    dict_arr.append(("Indian Angel Network (IAN)","Indian Angel Network"))
    return dict(dict_arr)
 
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
 
def resolveInvestor(investor,inv_map):
       
    if investor in inv_map:
        return inv_map[investor]
   
    return investor
 
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
 
df.InvestorsName.fillna('blank',inplace=True)
df.InvestorsName = df.InvestorsName[(df.InvestorsName != 'Undisclosed Investors') & (df.InvestorsName != 'Undisclosed investors')]
 
investors = []
inv_map   = getInvestorMap()
for investor in df.InvestorsName:
    for ele in getInvestor(investor):
        ele = resolveInvestor(ele.strip(),inv_map)
        temp = ele.strip().lower()
        if temp != '' and temp != 'nan' and temp != 'others' and temp != 'other':
            investors.append(ele.strip().title())
 
inv_df = pd.DataFrame(investors,columns=['InvestorName'])
groupcols = inv_df.InvestorName.value_counts()
for investor in groupcols.keys()[:5]:
    print(investor,groupcols[investor])
 
 
 