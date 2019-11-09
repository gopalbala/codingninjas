import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
res = np.where(a%2 == 1)
print(res[0])
for i in res[0]:
    a[i] = -1
print(*a)

ar = np.array([11, 2, 13, 4, 15, 6, 27, 8, 19])
idx = np.where(ar == np.max(ar))[0]
print(idx)
ar[idx[0]] = 0
for i in ar:
    print(i)

a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a1[3:9] = -1*a1[3:9]
print(a1)