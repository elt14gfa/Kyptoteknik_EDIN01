import numpy as np


A = [0, 1, 2, 3, 4, 5]

B = [0,1,2,3,4,5]

currentState = [1,0,0,1]
c0=currentState[0]
c3 = currentState[3]
currentState = currentState[1:]
currentState.append((c0+c3) % 2)

if np.array_equal(A,B):
    print('hej')

print(currentState)






assert (len(A) == 6)

print(A)

res = list(map(lambda a, b: str(int(a) * 5 + int(b)), A,B))

print(res)

for r,c in zip(A,B):
    print('r', r)
    print('c', c)


