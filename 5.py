"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

from functools import reduce
from math import gcd


def lcm(a: int, b: int):
    'least common multiple of x and y'
    return abs(a * b) // gcd(a, b)


limit = 20


def initial_solve(limit):
    pass


def improved_solve(limit):
    pass


def cheaty_solve(limit):
    return reduce(lcm, range(1, limit + 1))


# 232792560
# print(initial_solve(digit))
# print(improved_solve(digit))
print(cheaty_solve(limit))
