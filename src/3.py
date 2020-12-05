"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from itertools import takewhile
from math import floor, sqrt


number = 600851475143


def initial_solve(number):
    while True:
        for i in range(2, number):
            if number % i == 0:
                number //= i
                break
        else:
            return number, count


def improved_solve(number):
    while True:
        for i in range(2, floor(sqrt(number)) + 1):
            if number % i == 0:
                number //= i
                break
        else:
            return number


# 6857
print(initial_solve(number))
print(improved_solve(number))
