import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

df1 = df[(df['Species']=='Iris-setosa')].reset_index(drop=True)
df2 = df[(df['Species']=='Iris-versicolor')].reset_index(drop=True)
df3 = df[(df['Species']=='Iris-virginica')].reset_index(drop=True)
 
print('%.2f'%(df1['SL'].min()), '%.2f'%(df1['SW'].min()), '%.2f'%(df1['PL'].min()),'%.2f'%(df1['PW'].min()), 'Iris-setosa')
print('%.2f'%(df1['SL'].max()), '%.2f'%(df1['SW'].max()), '%.2f'%(df1['PL'].max()),'%.2f'%(df1['PW'].max()), 'Iris-setosa')
print('%.2f'%(df1['SL'].mean()), '%.2f'%(df1['SW'].mean()),'%.2f'%(df1['PL'].mean()),'%.2f'%(df1['PW'].mean()),'Iris-setosa')

print('%.2f'%(df2['SL'].min()), '%.2f'%(df2['SW'].min()), '%.2f'%(df2['PL'].min()),'%.2f'%(df2['PW'].min()), 'Iris-versicolor')
print('%.2f'%(df2['SL'].max()), '%.2f'%(df2['SW'].max()), '%.2f'%(df2['PL'].max()),'%.2f'%(df2['PW'].max()), 'Iris-versicolor')
print('%.2f'%(df2['SL'].mean()), '%.2f'%(df2['SW'].mean()),'%.2f'%(df2['PL'].mean()),'%.2f'%(df2['PW'].mean()),'Iris-versicolor')
 
print('%.2f'%(df3['SL'].min()), '%.2f'%(df3['SW'].min()), '%.2f'%(df3['PL'].min()),'%.2f'%(df3['PW'].min()), 'Iris-virginica')
print('%.2f'%(df3['SL'].max()), '%.2f'%(df3['SW'].max()), '%.2f'%(df3['PL'].max()),'%.2f'%(df3['PW'].max()), 'Iris-virginica')
print('%.2f'%(df3['SL'].mean()), '%.2f'%(df3['SW'].mean()),'%.2f'%(df3['PL'].mean()),'%.2f'%(df3['PW'].mean()),'Iris-virginica')