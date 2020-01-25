import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]

reg_name =  ['Delhi NCR', 'Rest of India']
res_count = [df_NCR.City.count(),df_ROI.City.count()]
plt.bar(reg_name,res_count,edgecolor='black',width=0.6)
plt.title('Restaurants - Delhi NCR vs Rest of India')
plt.xlabel('Region')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=40)
plt.show()


