import math
import sys
import numpy as np
import functools
from operator import mul
from operator import add

our_N = 170527948450228765165631
test_N = 323
L = 1000
F = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
xStore = []

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

nbrPrimes = storePrimes(990)

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
    nbrPrimes = storePrimes(990)

    binaryVector = np.zeros((len(nbrPrimes)))
    count = 0
    oddOrEven = 0
    for j in range(0, len(rVector)):
        if rVector[j] == nbrPrimes[count]:
            oddOrEven += 1

        else:
            if oddOrEven % 2 == 1:
                binaryVector[count] = 1
            oddOrEven = 1
            count += 1

            while rVector[j] != nbrPrimes[count]:
                oddOrEven = 1
                count += 1
            try:
                if rVector[j + 1] != None:
                    pass
            except IndexError:
                if rVector[j] == nbrPrimes[count]:
                    binaryVector[count] = 1
    return binaryVector

def getFactorizedList():
    #nbrPrimes
    listFactorized = []
    listOfBinaryR = []
    chosen_r_values = []
    binaryM = None
    #binaryM = np.zeros((1, len(F)))
    counter = 0
    for k in range(2, 20):
        for j in range(2, 15):
            r = int(math.sqrt(k * test_N)) + j
            list = []
            rsquared_modN = (r * r) % test_N
            factorized = primeFactorization(rsquared_modN, list)
            for prime in factorized:
                isValid = True
                if prime not in nbrPrimes:
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


def findSolution(binaryMatrix, element = 0, xSolution = np.eye(L,L), isNotZero = True):
    #nbrPrimes
    rowCounterToRemove = 0

    if L - len(nbrPrimes) != len(binaryMatrix) or isNotZero:
        for row in binaryMatrix:
            rowIterator = 0
            try:
                if row[element] == 1:
                    binaryMatrixEdited = np.delete(binaryMatrix, np.s_[0:rowCounterToRemove + 1], 0)
                    rowIterator = rowCounterToRemove + 1
                    for row1 in binaryMatrixEdited:
                        if row1[element] == 1:
                            additionRow = np.array(row)
                            additionRow1 = np.array(row1)
                            binaryMatrix[rowIterator] = (additionRow + additionRow1) % 2
                            xSolution[rowIterator] = (xSolution[rowIterator] + xSolution[rowCounterToRemove]) % 2
                        rowIterator += 1
                else:
                    rowCounterToRemove += 1
            # print(binaryMatrix, '\n')

            except IndexError:
                break

            if rowIterator == (L - element) or rowIterator == len(binaryMatrix):
                xSolution = np.delete(xSolution, rowCounterToRemove, 0)
                binaryMatrix = np.delete(binaryMatrix, rowCounterToRemove, 0)
                element += 1
                rowCounterToRemove = 0
                findSolution(binaryMatrix, element, xSolution, isNotZero)
                break
            elif rowCounterToRemove == len(binaryMatrix):
                element += 1
                rowCounterToRemove = 0
                findSolution(binaryMatrix, element, xSolution, isNotZero)
                break
            elif np.count_nonzero(binaryMatrix) == 0:
                xStore.append(xSolution)
                isNotZero = False
                return xSolution

    return xStore


def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

def multiplicationOfSolutions(resultsVector, r_values, factorized_values):
    print('resultVector :', '\n', resultsVector)
    prime_factor1 = 0
    prime_factor2 = 0
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
    binaryM, chosen_r_values, listFactorized = (getFactorizedList())
    print('bM', binaryM)
    print('r_values', chosen_r_values)
    print('list', listFactorized)
    x = findSolution(binaryM)[0]

    #resultsVector = [[1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]]
    #resultsVector1 = [[0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]
    prime1, prime2 = multiplicationOfSolutions(x, chosen_r_values, listFactorized)
    print('Prime factor 1: ', prime1)
    print('Prime factor 2: ', prime2)






