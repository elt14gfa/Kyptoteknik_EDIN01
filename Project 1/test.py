import numpy as np
from operator import add
from operator import mul
import functools


<<<<<<< HEAD

yx = np.eye(5,5)

print(yx)

x = np.delete(yx, np.s_[0:1], 0)
=======
list = [2, 2, 2, 2, 1, 1, 2, 10]
prod = functools.reduce(mul, list, 1)
print(prod)


>>>>>>> 7ef9e55c417669768fad1e967fd05f1ea85c7a90

print(x)

