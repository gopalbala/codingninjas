import pandas as pd
cols =['SepalLengh','SepalWidth','PetalLength','PetalWidth','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

irsen = df[df.Species == 'Iris-virginica'] # and df.PetalLength > 1.5]
ir15 = irsen[irsen.PetalLength>1.5]
# list(ir15)
# CountsDf = df['Species'].value_counts()
# keys = CountsDf.keys().tolist()
# count = CountsDf.tolist()
print(ir15.to_string(header=False))