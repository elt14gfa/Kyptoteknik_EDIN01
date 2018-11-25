import numpy as np
from operator import add
from operator import mul

s = 0

s = np.zeros(12)
print('s', s)


b = np.eye(5,5)
b[1][0] = 2
print(b)


a = [[0,1,1,1,1],[1,1,1,1,1]]
yx = np.eye(5,5)
print(a)
print(len(a))
a = [1, 1, 1, 1, 1]
k=5
for i in range(0,k):
    print(k)
    k -= 1


