import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]

df['Restaurant Name'] = df['Restaurant Name'].apply(lambda x:'Giani' if x=="Giani's" else x)
outlet_dtl = df['Restaurant Name'].value_counts()
restaurants = outlet_dtl.keys()[:15].tolist()
outlets     = outlet_dtl[:15].tolist()
  
plt.bar(restaurants,outlets)
plt.xlabel('Restaurant')
plt.ylabel('outlets')
plt.xticks(rotation=90)
plt.title('Number of Outlets for Top Restaurants')
plt.show()
