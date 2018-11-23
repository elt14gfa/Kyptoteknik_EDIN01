import math
import sys
import numpy as np

our_N = 170527948450228765165631
test_N = 16637
L = 12
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


    binaryM = np.zeros((L, len(F)))
    for i in range(0, len(rList)):
        count = 0
        oddOrEven = 0
        for j in range(0, len(rList[i])):
            if rList[i][j] == F[count]:
                oddOrEven += 1

            else:
                if oddOrEven % 2 == 1:

                    binaryM[i][count] = 1
                oddOrEven = 1
                count += 1

                while rList[i][j] != F[count]:
                    oddOrEven = 1
                    count += 1
                try:
                    if rList[i][j+1] != None:
                        pass
                except IndexError:
                    if rList[i][j] == F[count]:

                        binaryM[i][count] = 1
    return binaryM

#print(binaryMatrix(listOfR))

def newRFitForMatrix(rVector):
    nbrPrimes = storePrimes(1000)

    binaryVector = np.zeros((len(F)))
    count = 0
    oddOrEven = 0
    for j in range(0, len(rVector)):
        if rVector[j] == F[count]:
            oddOrEven += 1

        else:
            if oddOrEven % 2 == 1:
                binaryVector[count] = 1
            oddOrEven = 1
            count += 1

            while rVector[j] != F[count]:
                oddOrEven = 1
                count += 1
            try:
                if rVector[j + 1] != None:
                    pass
            except IndexError:
                if rVector[j] == F[count]:
                    binaryVector[count] = 1
    return binaryVector

def getFactorizedList():
    binaryM = None
    #binaryM = np.zeros((1, len(F)))
    counter = 0
   # for k in range(2, 20):
   #     for j in range(2, 15):
    #r = int(math.sqrt(k * test_N)) + j
    r1 = [225,261,291,292,317,343,413,431,458,469,473,395,490]
    for r in r1:
        list = []
        rsquared_modN = (r * r) % test_N
        factorized = primeFactorization(rsquared_modN, list)
        for item in factorized:
            isValid = True
            if item not in F:
                isValid = False
        if isValid and counter <= L - 1:
            binaryR = newRFitForMatrix(factorized)
            print(r, factorized)
            if binaryM is None:
                binaryM = binaryR
                counter += 1
            else:
                if counter == 1:
                    if np.array_equal(binaryR,binaryM):
                        exists = True
                    else:
                        exists = False
                else:
                    for row in binaryM:
                        exists = False
                       # if (binaryR == row).all():
                        if np.array_equal(binaryR,row):
                            exists = True
                            break
                # print('binary R: ', binaryR)
                if exists == False:
                    binaryM = np.vstack([binaryM, binaryR])
                    counter += 1

                    #print('k: ', k, 'j: ', j)
                    # print('r squared: ', rsquared_modN)
                    #listOfR.append(factorized)

    return binaryM


if __name__ == '__main__':

    nbrFactored = test_N
    print(getFactorizedList())


