# This program is a solution for
# Project Euler Problem 51
# https://projecteuler.net/problem=51

# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.


from sympy import isprime


def primeDigitReplacements(number):
    listOfNine = []
    number = list(str(number))
    for first in range(0, len(number)):
        for second in range(first + 1, len(number)):
            for third in range(second + 1, len(number)):
                for sameDigit in range(0, 10):
                    if sameDigit == 0 and first == 0:  # first digit can't be 0
                        continue
                    newNumber = number.copy()
                    for change in first, second, third:
                        # replaces digits with new same digit
                        newNumber.pop(change)
                        newNumber.insert(change, str(sameDigit))
                    newNumber = int("".join(newNumber))
                    listOfNine.append(newNumber)
                numberOfPrime = 0
                for i in listOfNine:
                    if isprime(i):
                        numberOfPrime += 1
                if numberOfPrime == 8:
                    return listOfNine
                listOfNine = []
    return False


n = 56993  # which is the last member of seven prime value family
while True:
    n += 1
    if primeDigitReplacements(n):
        # 8 of 9 are prime, controls which is the smallest, first or second
        print(primeDigitReplacements(n)[0] if primeDigitReplacements(n)[0] else primeDigitReplacements(n)[1])
        break
