import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()

NCR_cities = ['New Delhi', 'Faridabad', 'Ghaziabad', 'Noida', 'Gurgaon']
df_NCR = df[(df.City.isin(NCR_cities)) & (df['Country Code'] == 1)]
df_ROI = df[(df.City.apply(lambda x: False if x in NCR_cities else True)) & (df['Country Code'] == 1)]


NCR_Cuisines = []
for cuisine in df_NCR.Cuisines: 
    NCR_Cuisines.extend([x.strip() for x in cuisine.split(',')])
df_NCR_Cuisines = pd.DataFrame(NCR_Cuisines,columns=['Cuisine'])
NCR_Cuisine_freq = df_NCR_Cuisines.Cuisine.value_counts()
print('Top 10 NCR Cuisines:' )
for cuisine in NCR_Cuisine_freq.keys()[:10]: 
    print(cuisine, NCR_Cuisine_freq[cuisine])
plt.title('NCR Cuisines')
plt.pie(NCR_Cuisine_freq[:10],labels=NCR_Cuisine_freq.keys()[:10],autopct='%.1f%%')
plt.axis('equal')
plt.show()

ROI_Cuisines = []
for cuisine in df_ROI.Cuisines: 
    ROI_Cuisines.extend([x.strip() for x in cuisine.split(',')])
df_ROI_Cuisines = pd.DataFrame(ROI_Cuisines,columns=['Cuisine'])
ROI_Cuisine_freq = df_ROI_Cuisines.Cuisine.value_counts()
print()
print('Top 10 ROI Cuisines:' )
for cuisine in ROI_Cuisine_freq.keys()[:10]:
    print(cuisine,ROI_Cuisine_freq[cuisine])
    
plt.title('ROI Cuisines')
plt.pie(ROI_Cuisine_freq[:10],labels=ROI_Cuisine_freq.keys()[:10],autopct='%.1f%%')
plt.axis('equal')
plt.show()
