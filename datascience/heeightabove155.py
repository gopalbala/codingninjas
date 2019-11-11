## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np

age=np.array([15,17,19,20,14,21,16,19,13,20,22,23,21,16,18,19,20,15,17,18])
height=np.array([156,144,180,162,152,157,154,155,151,150,158,179,126,182,183,154,159,160,172,149])

li = np.where(height > 155)
# print(age[li])
li = np.where(height > 155)
# print(age[li])
# print(li)
for i in li[0]:
    print(str(age[i]) + " "+ str(height[i]))

ar = np.array( [[21, 20, 19, 18, 17],
  [16, 15, 14, 13, 12],
  [11, 10,  9, 8,  7],
  [ 6,  5, 4,  3,  2]])

print(ar)
print(ar[ar[:,1].argsort()])