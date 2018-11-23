import math
import sys
import numpy as np

our_N = 170527948450228765165631
test_N = 16637
L = 1000
F = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# Store the first 'numberOfPrimes' prime numbers
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


def primeFactorization(number, primeFactors=[], prodAllFact=1):
    if prodAllFact != nbrFactored:
        for potentialPrime in range(1, number + 1):
            counter_divisions = 0
            if number % potentialPrime == 0:
                for j in range(1, potentialPrime + 1):
                    if potentialPrime % j == 0:
                        counter_divisions += 1
                if counter_divisions == 2:
                    primeFactors.append(potentialPrime)
                    number = int(number / potentialPrime)
                    prodAllFact *= potentialPrime
                    primeFactorization(number, primeFactors, prodAllFact)
                    break

    return primeFactors


"""
Input: List with r^2 mod N
Returns: Binary Matrix
"""

def binaryMatrix(rList):
    nbrPrimes = storePrimes(1000)


    binaryM = np.zeros((12, len(F)))
    for i in range(0, len(rList)):
        count = 0
        oddOrEven = 0
        for j in range(0, len(rList[i])):
            if rList[i][j] == F[count]:
                oddOrEven += 1
                print('equal')
            else:
                if oddOrEven % 2 == 1:
                    print('adding', F[count])
                    binaryM[i][count] = 1
                oddOrEven = 1
                count += 1
                print(rList[i][j], F[count])

                while rList[i][j] != F[count]:
                    oddOrEven = 1
                    count += 1
                try:
                    if rList[i][j+1] != None:
                        pass
                except IndexError:
                    if rList[i][j] == F[count]:
                        print('adding', F[count])
                        binaryM[i][count] = 1



    return binaryM

rList = [[2, 3, 7, 17], [11, 11, 13], [2, 2, 2, 11, 17], [3, 3, 3, 7, 11]]
# print(rList[0][0])
print(binaryMatrix(rList))

nbrFactored = 9
# print(primeFactorization(nbrFactored))

# print(binaryMatrix())

ourPrimes = storePrimes(10)
listOfR = []
counter = 1
for k in range(2, 20):
    for j in range(2, 15):
        list = []
        r = int(math.sqrt(k * test_N)) + j
        rsquared_modN = (r * r) % test_N
        factorized = primeFactorization(rsquared_modN, list)
        for item in factorized:
            isValid = True
            if item not in ourPrimes:
                isValid = False

        if isValid and counter <= L and factorized not in listOfR:
            # print('k: ', k, 'j: ', j)
            # print('r squared: ', rsquared_modN)
            listOfR.append(factorized)
            counter += 1
print(listOfR)

