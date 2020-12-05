"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from itertools import takewhile
from math import ceil, floor, sqrt


index = 10_001


def initial_func(index):
    prime_numbers = []
    a = 1

    while True:
        a += 2
        for prime in prime_numbers:
            if a % prime == 0:
                break
        else:
            prime_numbers.append(a)
            if len(prime_numbers) == index - 1:
                break

    return prime_numbers[-1]


def improved_func(index):
    prime_numbers = []
    a = 1

    while True:
        a += 2
        for prime in takewhile(lambda x: x <= sqrt(a), prime_numbers):
            if a % prime == 0:
                break
        else:
            prime_numbers.append(a)
            if len(prime_numbers) == index - 1:
                break

    return prime_numbers[-1]


# 104743
print(initial_func(index))
print(improved_func(index))
