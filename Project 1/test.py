import numpy as np
from operator import add
from operator import mul
import functools
import math


def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)

def storePrimes(numberOfPrimes):
    primes = []
    for potentialPrime in range(2, 7829 + 1):
        prime = True
        for number in range(2, potentialPrime):
            if potentialPrime % number == 0:
                prime = False
                break
        if prime:
            primes.append(potentialPrime)
        if len(primes) == numberOfPrimes:
            break
    return primes

if __name__ == '__main__':

    nbr = 160


    while(nbr % 2 == 0):
        nbr = nbr / 2
        print(nbr)

    list = []
    vec = [1,0,0,0,1,1]
    vec1 = [1,0,0,0,1,1]

    list.append(vec1)
    list.append(vec)
    print(list)
    primes = storePrimes(100)
    print(primes)
    print(primes[-1])


    diff = 516582682
    N = 3205837387
    #print(gcd(diff,N))
    arr = np.eye(10,10)
    arr[1][1] = 0
    print('arr', '\n', arr)

    if np.count_nonzero(arr[0:][1]) == 0:
        print(arr[0:][1])
        print(arr[0:][0])
        print('hej')

    for i in range(0,10):
        print(i)
        for j in range(0,10):
            print(j)
            if j == 5:
                print('jjjjjjj')
                break
        print('kkkkk')

    y = np.array([[2,2,3,5,7,11],[1,0,0,1,0,0],[1,1,1,1,0,1]])
    print(y)
    x = [4]
    print(y[:,0])

    print('func', functools.reduce(mul, x,1))

    L = 300

    b = np.zeros((133,100))

    print(np.shape(b))
    r, c = np.shape(b)
    c = np.zeros((L-1-r,c))

    a = np.vstack([b,c])

    print(np.shape(a))
