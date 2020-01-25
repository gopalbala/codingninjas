import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(df,region):  
    City_dtl = {}
    for i in range(len(df)):
        curCity = df.City.iloc[i]
        if curCity not in City_dtl:
            City_dtl[curCity] = [0,0,0]
        City_dtl[curCity][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
        City_dtl[curCity][1] += df.Votes.iloc[i]
        City_dtl[curCity][2] += 1


    cities    = list(City_dtl.keys())
    wt_rating = [City_dtl[city][0]/City_dtl[city][1] for city in City_dtl]
    restaurants = [City_dtl[city][2] for city in City_dtl]

    colors = range(len(cities))
    plt.scatter(cities,restaurants,s=wt_rating,c=colors)
    plt.title('Bubble Graph Restaurants in '+region)
    plt.xlabel('City')
    plt.xticks(rotation=90)
    plt.ylabel('Number of restaurants')
    plt.show()

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]
plot_graph(df_ROI,'ROI')
plot_graph(df_NCR,'NCR')