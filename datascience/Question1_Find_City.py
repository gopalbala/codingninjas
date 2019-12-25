# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    ncr_list = ['Delhi', 'New Delhi', 'Gurgaon', 'Noida']
    if location.title() in ncr_list:
        city = 'NCR'
        return city
    else: 
        return location.strip().title()

data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df.CityLocation = df.CityLocation.apply(getCity)
ncr_list = ['Bangalore', 'Mumbai', 'NCR']
cities = df.CityLocation[df.CityLocation.isin(ncr_list)]

city_grp = cities.value_counts(dropna=True)
for city in city_grp.keys():
    print(city, city_grp[city])


plt.bar(city_grp.keys(), city_grp,width=0.6,edgecolor='black')
plt.ylabel('Number of Fundings')
plt.xlabel('Location')
plt.title('City Vs Number of Start up Funding')
plt.show()

