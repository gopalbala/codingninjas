import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df = df[df['Country Code']==216]
df1 = df.Cuisines.dropna().reset_index()
 
Cuisine_dict = {}
for i in range(len(df1['Cuisines'])):
    cuisines = df1.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = 1
        else: 
            Cuisine_dict[cuisine] +=1 

Cuisine_dtl = sorted(Cuisine_dict.items(),key=lambda x:x[1])[:-11:-1]
restaurants = [cuisine[1] for cuisine in Cuisine_dtl] 
cuisines    = [cuisine[0] for cuisine in Cuisine_dtl] 

plt.title('Top Cuisines in USA')
plt.pie(restaurants,labels=cuisines,autopct='%.1f%%')
plt.axis('equal')
plt.show()
