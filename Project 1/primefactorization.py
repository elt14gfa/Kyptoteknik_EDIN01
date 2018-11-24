import math
import sys
import numpy as np
import functools
from operator import mul
from operator import add

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
    listFactorized = []
    listOfBinaryR = []
    chosen_r_values = []
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
        for prime in factorized:
            isValid = True
            if prime not in F:
                isValid = False
        if isValid and counter <= L - 1 and factorized not in listFactorized:
            binaryR = newRFitForMatrix(factorized)
            if not any((binaryR == x).all() for x in listOfBinaryR): # checks if the binary row already exists in the list
                chosen_r_values.append(r)
                listOfBinaryR.append(binaryR)
                listFactorized.append(factorized)
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

    return binaryM, chosen_r_values, listFactorized


def findSolution(binaryMatrix):
    return

def getRowIndex(matrix, findRow):
    counter = 0
    for row in matrix:
        if np.array_equal(row, findRow):
            break
        else:
            counter += 1

    return counter

def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

def multiplicationOfSolutions(resultsVector):
    prime_factor1 = 0
    prime_factor2 = 0
    matrix, r_values, factorized_values = getFactorizedList()
    print('Values of r: ', r_values)
    print('factorized_values: ', factorized_values)
    for xresult in resultsVector:
        r = 1
        y= 1
        counter = 0
        for index in xresult:
            if index == 1:
                y *= functools.reduce(mul, factorized_values[counter]) # product of array

                r *= r_values[counter]
            counter += 1
        r_modulo = r % test_N
        y_sqrt = math.sqrt(y)
        y_modulo = int(y_sqrt % test_N)
        # print(r_modulo)
        # print(y_modulo)
        if y_modulo > r_modulo:
            result = computeGCD(y_modulo - r_modulo, test_N)
        else:
            result = computeGCD(r_modulo - y_modulo, test_N)

        if result != 1:
            prime_factor1 = int(test_N/result)
            prime_factor2 = int(test_N/prime_factor1)

    return prime_factor1, prime_factor2



if __name__ == '__main__':
    nbrFactored = test_N
    resultsVector = [[1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]]
    prime1, prime2 = multiplicationOfSolutions(resultsVector)
    print('Prime factor 1: ', prime1)
    print('Prime factor 2: ', prime2)
    """
    binaryMatrix = (getFactorizedList())
    element = 0
    rowCounterToRemove = 0

    for row in binaryMatrix:
        rowIterator = 0

        try:
            if row[element] == 1:
                for row1 in binaryMatrix:
                    if getRowIndex(binaryMatrix, row1) > getRowIndex(binaryMatrix, row):
                        if row1[element] == 1:
                            additionRow = np.array(row)
                            additionRow1 = np.array(row1)
                            binaryMatrix[rowIterator] = (additionRow + additionRow1) % 2
                            #print(binaryMatrix)
                    rowIterator += 1
            else:
                rowCounterToRemove += 1


        # print(binaryMatrix, '\n')

        except IndexError:
            break

        if rowIterator == L - element:
            binaryMatrix = np.delete(binaryMatrix, rowCounterToRemove, 0)
            element += 1
            rowCounterToRemove = 0
"""



