import numpy as np
from operator import add


def getRowIndex(matrix, findRow):
    counter = 0
    for row in matrix:
        if np.array_equal(row, findRow):
            break
        else:
            counter += 1

    return counter


arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
index = getRowIndex(arr, [1,2,3,5])
print('The row is on index: ', index)



