"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from itertools import takewhile
from math import sqrt


limit = 2_000_000


def initial_solve(limit):
    result = 2
    prime_numbers = [2]
    a = 3

    while a < limit:
        for prime in prime_numbers:
            if a % prime == 0:
                break
        else:
            prime_numbers.append(a)
            result += a

        a += 2
        print(a)

    return result


def improved_solve(limit):
    result = 2
    prime_numbers = []
    a = 3

    while a < 2_000_000:
        for prime in takewhile(lambda x: x <= sqrt(a), prime_numbers):
            if a % prime == 0:
                break
        else:
            prime_numbers.append(a)
            result += a

        a += 2

    return result


# 142913828922
print(initial_solve(limit))
print(improved_solve(limit))
