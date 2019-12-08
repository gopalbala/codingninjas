import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
df1 = df[df.State == 'Jammu and Kashmir']
city_group = df1['City'].value_counts()
city_name  = city_group.keys()[0]
city_attacks = city_group[0]

city_df = df1[(df1.City == city_name) & (df1.Group != 'Unknown')]
grp_group  = city_df['Group'].value_counts()
print(city_name, city_attacks,grp_group.keys()[0])