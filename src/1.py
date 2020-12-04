"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

limit = 1000


def initial_solve(limit):
    result = 0

    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


def improved_solve(limit):
    pass


def cheaty_solve(limit):
    result = 0
    limit -= 1

    threes = limit // 3
    result += 3 * threes * (threes + 1) // 2

    fives = limit // 5
    result += 5 * fives * (fives + 1) // 2

    fifteens = limit // 15
    result -= 15 * fifteens * (fifteens + 1) // 2

    return result


# 233168
print(initial_solve(limit))
# print(improved_solve(limit))
print(cheaty_solve(limit))
