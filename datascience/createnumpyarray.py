import numpy as np

ar = np.array((1,10),dtype=int)

ar1 = np.empty(10,dtype=int)
ar1.fill(0)

ar2 = np.full(10,0,int)

ar2[4] = 1
ar2[9] = 1
print(ar2)

print(np.arange(10))

a = np.array([0, 1, 2, 3])
print(a.shape)

print(np.random.rand())

print(np.random.randint(10,size = (4,4)))

print(np.arange(9,50))

import numpy as np
id = np.eye(5,6,dtype=int)

a = np.array(id,dtype=int)

print(round(5/9),2)
a = np.array( round(5/9,2),dtype=float)
print(a)

k = round(5/9,2)
i = 1
while k < 5.0:
    print(k)
    i+=1
    k*=2
    
dar = np.arange (round(5/9,2),5,round(5/9,2),dtype=float)
print(dar)