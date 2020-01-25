import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1) & (df['Rating text'] != 'Not rated') & (df['Aggregate rating'] != 0)].dropna()
rating = df['Aggregate rating'].tolist()
plt.hist(rating,bins=10,edgecolor='black')
plt.xlabel('Aggregate Rating')
plt.ylabel('Number of Restaurants')
plt.title('Histogram of Aggregate Rating')
plt.grid()
plt.show()