import math
import sys
import numpy as np
import functools
from operator import mul
from operator import add
import timeit
from collections import Counter


our_N = 170527948450228765165631
test_N = 392742364277
L = 700
xStore = []

# Store the first 'numberOfPrimes' prime numbers, maximum up to the 990th prime
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

def primeFactorization(number):
    initNbr = number
    potentialPrimes = []
    prodAllPrimes = 1
    sqrtNbr = int(math.sqrt(initNbr))
    for prime in nbrPrimes:
        if prime <= sqrtNbr:
            while(number % prime == 0):

                potentialPrimes.append(prime)
                prodAllPrimes *= prime
                number = number / prime

        if prodAllPrimes == initNbr:
            return potentialPrimes
    if prodAllPrimes != initNbr:
        potentialPrimes.append(initNbr)
        return potentialPrimes


def newRFitForMatrix(rVector):

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
    maxPrime = nbrPrimes[-1]
    #nbrPrimes
    listFactorized = []
    listOfBinaryR = []
    chosen_r_values = []
    binaryM = None
    #binaryM = np.zeros((1, len(F)))
    counter = 1
    enter = True
    for k in range(2, 110):
        for j in range(2, 95):
            if counter == L+1:
                break
            if counter % 75 == 0 and enter == True:
                enter = False
                print(counter)
            r = int(math.sqrt(k * test_N)) + j
            list = []
            rsquared_modN = (r * r) % test_N
            factorized = primeFactorization(rsquared_modN)
            isValid = True
            if factorized[-1] <= maxPrime:
                isValid = False
                if counter <= L + 1 and factorized not in listFactorized:
                    binaryR = newRFitForMatrix(factorized)
                if not any((binaryR == x).all() for x in listOfBinaryR): # checks if the binary row already exists in the list
                    enter = True
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
                    if exists == False:
                        binaryM = np.vstack([binaryM, binaryR])

                        counter += 1



    return binaryM, chosen_r_values, listFactorized


def findSolution(binaryMatrix, element=0, xSolution=np.eye(L, L), isNotZero=True):
    rowCounterToRemove = 0
    if L - len(nbrPrimes) != len(binaryMatrix) or isNotZero:
        try:
            arrCheckForOnes = np.count_nonzero(binaryMatrix[:, element])
            if arrCheckForOnes >= 1:
                for row in binaryMatrix:
                    rowIterator = 0

                    if row[element] == 1:
                        foundAOne = 1
                        if arrCheckForOnes >= 2:
                            binaryMatrixEdited = np.delete(binaryMatrix, np.s_[0:rowCounterToRemove + 1], 0)
                            rowIterator = rowCounterToRemove + 1
                            for row1 in binaryMatrixEdited:
                                if foundAOne < arrCheckForOnes:
                                    if row1[element] == 1:
                                        foundAOne += 1
                                        additionRow = np.array(row)
                                        additionRow1 = np.array(row1)
                                        binaryMatrix[rowIterator] = (additionRow + additionRow1) % 2
                                        xSolution[rowIterator] = (xSolution[rowIterator] + xSolution[
                                            rowCounterToRemove]) % 2
                                else:
                                    break
                                rowIterator += 1

                        xSolution = np.delete(xSolution, rowCounterToRemove, 0)
                        binaryMatrix = np.delete(binaryMatrix, rowCounterToRemove, 0)
                        if np.count_nonzero(binaryMatrix) == 0:
                            xStore.append(xSolution)
                            isNotZero = False
                            break
                        element += 1
                        findSolution(binaryMatrix, element, xSolution, isNotZero)
                        break
                    else:
                        rowCounterToRemove += 1
                # print(binaryMatrix, '\n')
            else:
                element += 1
                rowCounterToRemove = 0
                if np.count_nonzero(binaryMatrix) == 0:
                    print(binaryMatrix)
                if np.count_nonzero(binaryMatrix) == 0:
                    isNotZero = False
                else:
                    findSolution(binaryMatrix, element, xSolution, isNotZero)
        except IndexError:
            return xStore

    return xStore

def multiplicationOfSolutions(resultsVector, r_values, factorized_values):
    prime_factor1 = 0
    prime_factor2 = 0
    print(np.shape(factorized_values))
    for xresult in resultsVector:
        y_exponents = Counter()
        half_y = Counter()
        y_product = 1
        y_sqrt = 1
        r = 1
        y= 1
        counter = 0
        for index in xresult:
            if index == 1:
                y_exponents += Counter(factorized_values[counter])
                yEdited = math.sqrt(functools.reduce(mul, factorized_values[counter], 1))
                y *= yEdited
                #y *= functools.reduce(mul, factorized_values[counter]) # product of array
                #y = int(math.sqrt(int(y)) % test_N)
                #y = int(math.sqrt(y))
                r *= r_values[counter]
            counter += 1

        for prime in nbrPrimes:
            y_exponents[prime] = int(y_exponents[prime]/2)
            y_product *= prime**y_exponents[prime]

        y_modulo_new = y_product % test_N
        # y_modulo = int(y_sqrt % test_N)
        # y_modulo = y % test_N
        r_modulo = r % test_N

        #y_sqrt = int(math.sqrt(y))
        #y_modulo = int(y % test_N)

        if y_modulo_new > r_modulo:

            # result = computeGCD(y_modulo - r_modulo, test_N)
            result = gcd(y_modulo_new - r_modulo, test_N)
        else:
            # result = computeGCD(r_modulo - y_modulo, test_N)
            print('r_modulo: ', r_modulo, ' y_modulo: ', y_modulo_new)
            result = gcd(r_modulo - y_modulo_new, test_N)

        if result != 1:
            prime_factor1 = int(test_N / result)
            prime_factor2 = int(test_N / prime_factor1)
            break

    return prime_factor1, prime_factor2


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b

    return gcd(b, a % b)



if __name__ == '__main__':


    nbrPrimes = storePrimes(L-10)
    nbrFactored = test_N
    start = timeit.default_timer()
    binaryM, chosen_r_values, listFactorized = (getFactorizedList())
    stop = timeit.default_timer()
    print('Time factorized: ', stop - start)
    print('L: ', L)
    print('shape r- values:', np.shape(chosen_r_values))
    if(len(chosen_r_values) == L):
            print('shape listfactorized', np.shape(listFactorized))
            print('shape binaryM: ', np.shape(binaryM))
            # print('r_values', chosen_r_values)
            # print('list', listFactorized)

            print('--------------------------------------------------------------------------------------------')
            # Your statements here
            r, c = np.shape(binaryM)
            start1 = timeit.default_timer()
            x = findSolution(binaryM, 0, np.eye(r, r))[0]
            stop1 = timeit.default_timer()
            print('Time solution: ', stop1 - start1)
            print('shape of x', np.shape(x))
            print('--------------------------------------------------------------------------------------------')
            # resultsVector = [[1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]]
            # resultsVector1 = [[0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]
            start2 = timeit.default_timer()
            prime1, prime2 = multiplicationOfSolutions(x, chosen_r_values, listFactorized)
            stop2 = timeit.default_timer()
            print('Time multi: ', stop2 - start2)
            print('Prime factor 1: ', prime1)
            print('Prime factor 2: ', prime2)
            if prime1 * prime2 == test_N:
                print('Successfully prime factorized')
    else:
        print('not enough values')









