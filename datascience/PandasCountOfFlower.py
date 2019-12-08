import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()
CountsDf = df['Species'].value_counts()
keys = CountsDf.keys().tolist()
count = CountsDf.tolist()
print(*count)