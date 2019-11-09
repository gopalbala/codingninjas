import numpy as np
input_=np.arange(1,21,1)
input_=input_.reshape(4,5)
print(input_)
out = input_[2,0:3]
print(*out)
out = input_[1:,3:4]
print(*out.flatten())
out = input_[2:,0:]
print(*out.flatten())
out = input_[1:3,1:3]
print(*out.flatten())