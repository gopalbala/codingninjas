import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

# find ranges for Votes 
cuisine_dict = {}
df['CuisineCount'] = df['Cuisines'].apply(lambda x: len(x.split(',')))
for i in range(len(df.CuisineCount)): 
    cuisinecnt = df.CuisineCount.iloc[i]
    if cuisinecnt not in cuisine_dict: 
        cuisine_dict[cuisinecnt] = [0,0]
    cuisine_dict[cuisinecnt][0]  += df['Aggregate rating'].iloc[i]
    cuisine_dict[cuisinecnt][1]  += 1

Cuis_Cnt_Arr = [x for x in cuisine_dict]
rating_arr = [cuisine_dict[x][0]/cuisine_dict[x][1] for x in cuisine_dict]

plt.bar(Cuis_Cnt_Arr, rating_arr)
plt.xlabel('Cuisine Count')
plt.ylabel('Rating')
plt.title('Effect of Cuisine Count on Rating')
plt.show()

