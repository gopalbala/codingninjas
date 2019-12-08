import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
gov_df = df[(df.Country=='India') & (df.Year >= 2014) & (df.Month > 0)]
gov_df['YearMonth'] = gov_df.Year * 10000 + gov_df.Month*100 + gov_df.Day
gov_df              = gov_df[(gov_df.YearMonth >= 20140526)]
attacks   = gov_df.YearMonth.count()
att_counts = gov_df['Group'].value_counts()
for group in att_counts.keys():
    if group != 'Unknown':
        act_group = group
        break
print(int(attacks), act_group)