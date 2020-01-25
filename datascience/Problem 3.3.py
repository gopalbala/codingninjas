import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[df['Country Code']==1]
df['Restaurant Name'] = df['Restaurant Name'].apply(lambda x:'Giani' if x=="Giani's" else x)

df1 = df.groupby(['Restaurant Name'])['Votes'].sum().reset_index()
df1 = df1.sort_values(by=['Votes'],ascending=False)[:10]
  
plt.bar(df1['Restaurant Name'],df1['Votes'])
plt.xlabel('Restaurant')
plt.ylabel('Votes')
plt.xticks(rotation=90)
plt.title('Number of Votes for Top Restaurants')
plt.show()

