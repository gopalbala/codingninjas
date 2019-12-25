import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
def getCity(location):
    location = str(location)
    if '/' in location:
        loc = location.split('/')
        location = loc[0]
   
    if location.title() == 'Delhi':
        city = 'New Delhi'
    else:
        city = location
    return city.strip().title()
 
data = pd.read_csv('startup_funding.csv')
df   = data.copy()
 
cities = df.CityLocation.apply(getCity)
 
freq = cities.value_counts(dropna=True)
i = 0
top_city = []
top_count = []
for city in freq.keys():
    if city == 'Nan':
        continue
    if i >= 10:
        break
    
    top_city.append(city)
    top_count.append(freq[city])
    i = i + 1
   
plt.pie(top_count,labels=top_city,autopct='%.2f%%')
plt.axis("equal")
plt.show()
 
for i in range(10):
    print(top_city[i],top_count[i])