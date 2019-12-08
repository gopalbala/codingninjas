import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
country_group = df['Country'].value_counts()
country_name  = country_group.keys()[0]
country_attacks = country_group[0]
country_df = df[(df.Country == country_name)]
year_group = country_df['Year'].value_counts()
print(country_name, country_attacks , year_group.keys()[0])