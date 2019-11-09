import numpy as np

a = np.array([1,2,0,0,4,0])
a1 = np.nonzero(a)
print(*a1[0])