"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from math import ceil, floor


digit = 3


def initial_func(digit):
    for i in range(10 ** (2 * digit), 10 ** (2 * digit - 2), -1):
        if f'{i}' == f'{i}'[::-1]:

            for f in range(100, 1000):
                if i % f == 0 and 1000 > i / f >= 100:
                    return i


def improved_func(digit):
    for i in range(10 ** (2 * digit), 10 ** (2 * digit - 2), -1):
        if f'{i}' == f'{i}'[::-1]:

            for f in range(max(10 ** (digit - 1), ceil(i / 10 ** digit)),
                           min(10 ** digit, floor(i / 10 ** (digit - 1)) + 1)):
                if i % f == 0:
                    return i


# 906609
print(initial_func(digit))
print(improved_func(digit))
