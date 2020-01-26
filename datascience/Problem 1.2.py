import matplotlib.pyplot as plt
import pandas as pd
import requests
import json 

def get_City_ID(city): 
    header = {'user-key':'xx'}
    indata   = {'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/cities',params=indata,headers=header)
    data  = json.loads(r.text)
    for city_info in data['location_suggestions']:
        if city_info['country_id'] == 1:
            return city_info['id']
        
    return 'NA'

def get_cuisines(city_id):
    header = {'user-key':'xx'}
    indata = {'city_id':city_id}
    r = requests.get('https://developers.zomato.com/api/v2.1/cuisines',params=indata,headers=header)
    data   = json.loads(r.text)
    cuisines = []
    for cuisine in data['cuisines']: 
        cuisines.append(cuisine['cuisine']['cuisine_name'])
    return cuisines
 
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend(cuisine.split(','))
    
NCR_Cuisine_Set = set(NCR_Cuisines)    

ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend(cuisine.split(','))
    
ROI_Cuisine_Set = set(ROI_Cuisines)    

## Cuisines present in ROI but not in NCR 
ROI_not_in_NCR = ROI_Cuisine_Set.difference(NCR_Cuisine_Set)   


## Check if the cuisines are really not present in NCR region
NCR_City_Id = []
for city in NCR_cities: 
    city_Id = get_City_ID(city)
    if city_Id != 'NA':
        NCR_City_Id.append(city_Id)

## get cuisines list of NCR region
NCR_Actual_Cuisines = []
for city_id in NCR_City_Id: 
    NCR_Actual_Cuisines.extend(get_cuisines(city_id))


print('as per dataset:')
print('      Cuisines in ROI but not present in NCR:',*ROI_not_in_NCR)
print()
print('As per zomato API:')
## Find cuisines that are actually not served in NCR: 
for ROI_Cuisine in ROI_not_in_NCR: 
    if ROI_Cuisine in NCR_Actual_Cuisines: 
        print(ROI_Cuisine)



