import math
import sys


our_N = 170527948450228765165631
test_N = 16637
L = 12

# Store the first 'numberOfPrimes' prime numbers
def StorePrimes(numberOfPrimes):
    primes = []
    for potentialPrime in range(2, 7829+1):
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

def primeFactorization(number, primeFactors):
    initNbr = number
    prodAllFact = 1
    for potentialPrime in range(1, number + 1):
        counter_divisions = 0
        if number % potentialPrime == 0:
            for j in range(1, potentialPrime + 1):
                if potentialPrime % j == 0:
                    counter_divisions += 1

            if counter_divisions == 2:
                primeFactors.append(potentialPrime)
                number = int(number / potentialPrime)
                primeFactorization(number, primeFactors)
                prodAllFact *= potentialPrime
                if prodAllFact == initNbr:
                    return primeFactors

    # return primeFactors


primeFactors = []
print(primeFactorization(16, primeFactors))

"""
for k in range(1, 100):
    for j in range(1, 100):
        r = int(math.sqrt(k*test_N)) + j
        print('k: ', k, ' j: ', j, ' r: ', r)
        rsquared_modN = r*r % test_N
        print(rsquared_modN)
        # if rsquared_modN factors is in [ourprimes]:
"""



