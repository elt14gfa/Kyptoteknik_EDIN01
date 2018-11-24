import numpy as np
from operator import add
from operator import mul
import functools


list = [2, 2, 2, 2, 1, 1, 2, 10]
prod = functools.reduce(mul, list, 1)
print(prod)




