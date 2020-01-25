import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

Cuisine_dict = {}
for i in range(len(df['Cuisines'])):
    cuisines = df.Cuisines.iloc[i]
    cuis_arr = cuisines.split(',')
    for cuisine in cuis_arr:
        cuisine=cuisine.strip().title()
        if cuisine not in Cuisine_dict: 
            Cuisine_dict[cuisine] = [0,0]
        Cuisine_dict[cuisine] = [Cuisine_dict[cuisine][0]+df['Aggregate rating'].iloc[i],Cuisine_dict[cuisine][1]+1]

Cuisine_list = list(Cuisine_dict.keys())
rating_list  = [Cuisine_dict[cuisine][0]/Cuisine_dict[cuisine][1] for cuisine in Cuisine_dict]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.title('Rating of Specific Cuisines')
plt.show()

Cuisine_rating = [[Cuisine_list[i],rating_list[i]] for i in range(len(Cuisine_list))]
Cuisine_rating.sort(key=lambda x:x[1])
Cuisine_list = [cuisinerate[0] for cuisinerate in Cuisine_rating[:-10:-1]]
rating_list  = [cuisinerate[1] for cuisinerate in Cuisine_rating[:-10:-1]]
plt.bar(Cuisine_list,rating_list)
plt.xlabel('Cuisine')
plt.ylabel('Rating')
plt.xticks(rotation=40)
plt.title('Rating of Top rated Specific Cuisines')
plt.show()
