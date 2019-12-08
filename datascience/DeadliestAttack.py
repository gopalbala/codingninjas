import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
ind = df.Killed.idxmax()
print(int(df.Killed[ind]), df.Country[ind], df.Group[ind])