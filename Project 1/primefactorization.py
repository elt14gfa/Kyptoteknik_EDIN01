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

def primeFactorization(number, primeFactors = [], prodAllFact = 1):
    initnumber = number
    print('initnumber: ', initnumber)
    print('allfrac: ', prodAllFact)
    if prodAllFact != initnumber:
        for potentialPrime in range(1, number + 1):
            print('number: ', potentialPrime)
            counter_divisions = 0
            if number % potentialPrime == 0:
                for j in range(1, potentialPrime + 1):
                    if potentialPrime % j == 0:
                        counter_divisions += 1

                if counter_divisions == 2:
                    print('added prime: ', potentialPrime)
                    primeFactors.append(potentialPrime)
                    print('number1: ', number)
                    number = int(number / potentialPrime)
                    print('number2: ', number)
                    prodAllFact *= potentialPrime
                    primeFactorization(number, primeFactors, prodAllFact)
                    break

    return primeFactors

    # return primeFactors
#primeFactors = []
initnumber = 9
print(primeFactorization(9))
#primeFactorization(16)

"""
for k in range(1, 100):
    for j in range(1, 100):
        r = int(math.sqrt(k*test_N)) + j
        print('k: ', k, ' j: ', j, ' r: ', r)
        rsquared_modN = r*r % test_N
        print(rsquared_modN)
        # if rsquared_modN factors is in [ourprimes]:
"""



