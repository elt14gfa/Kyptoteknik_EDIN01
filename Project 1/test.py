import numpy as np
from operator import add



yx = np.eye(5,5)

print(yx)

x = np.delete(yx, np.s_[0:1], 0)

print(x)

