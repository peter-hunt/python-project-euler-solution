"""
Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

from itertools import takewhile


def initial_solve():
    abundants = [
        i for i in range(12, 28124)
        if 1 + sum(j for j in range(2, i) if i % j == 0) > i
    ]

    sums = {*()}

    print('Started')

    for i in abundants:
        for j in takewhile(lambda n: n <= 28123 - i, abundants):
            if i + j <= 28123 and i + j not in sums:
                sums.add(i + j)

    return sum(i for i in range(1, 28124) if i not in sums)


def improved_solve():
    pass


# 4179871
print(initial_solve())
# print(improved_solve())
