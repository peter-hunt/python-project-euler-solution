"""
Sum square difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

from math import ceil, floor


length = 100


def initial_func(length):
    sum_of_square = 0
    sum_of_number = 0

    for i in range(1, length + 1):
        sum_of_square += i ** 2
        sum_of_number += i

    square_of_sum = sum_of_number ** 2

    return square_of_sum - sum_of_square


def improved_func(digit):
    pass


def cheaty_func(digit):
    length = 100

    square_of_sum = (length * (length + 1) // 2) ** 2
    sum_of_square = length * (length + 1) * (2 * length + 1) // 6

    return square_of_sum - sum_of_square


# 25164150
print(initial_func(length))
# print(improved_func(length))
print(cheaty_func(length))
