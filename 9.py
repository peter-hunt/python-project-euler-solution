"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import ceil, sqrt

total = 1_000


def initial_solve(total):
    for a in range(1, total):
        for b in range(1, total):
            c = sqrt(a ** 2 + b ** 2)
            if c % 1 == 0 and a + b + c == total:
                return a * b * int(c)


def improved_solve(total):
    for a in range(1, total):
        for b in range(ceil(sqrt(2 * a + 1)), total - a * 2):
            c = sqrt(a ** 2 + b ** 2)
            if c % 1 == 0 and a + b + c == total:
                return a * b * int(c)


def cheaty_solve(total):
    pass


# 31875000
print(initial_solve(total))
print(improved_solve(total))
# print(cheaty_solve(total))
