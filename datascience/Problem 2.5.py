import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zomato.csv',encoding='ISO-8859-1')
df = data.copy()
df= df[(df['Country Code'] == 1)].dropna()

Locality_dtl = {}
for i in range(len(df)):
    curLocality = df.Locality.iloc[i]
    if curLocality not in Locality_dtl:
        Locality_dtl[curLocality] = [0,0,0]
    Locality_dtl[curLocality][0] += df.Votes.iloc[i]*df['Aggregate rating'].iloc[i]
    Locality_dtl[curLocality][1] += df.Votes.iloc[i]


for locality in Locality_dtl:
    wt_rating_val = Locality_dtl[locality][0]/Locality_dtl[locality][1]
    Locality_dtl[locality] = wt_rating_val

Top_dtl = sorted(Locality_dtl.items(),key=lambda x:x[1])[:-11:-1]
for loc_info in Top_dtl: 
    print(*loc_info)
    
Localities    = [x[0] for x in Top_dtl]
wt_rating = [x[1] for x in Top_dtl]

plt.bar(Localities,wt_rating)
plt.title('Weighted Rating in each Locality')
plt.xlabel('Locality')
plt.xticks(rotation=75)
plt.ylabel('Weighted Rating')
plt.show()
