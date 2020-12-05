"""
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import floor, sqrt


limit = 10_000


def initial_func(limit):
    def sum_divisors(n):
        result = 1

        for i in range(2, floor(sqrt(n))):
            if n % i == 0:
                if i == n // i:
                    result += i
                else:
                    result += i + n // i

        return result

    amicables = {*()}
    result = 0

    for i in range(2, limit):
        if i in amicables:
            continue
        other = sum_divisors(i)
        if other == i:
            continue

        if sum_divisors(other) == i:
            amicables.add(i)
            result += i
            if other < limit:
                amicables.add(other)
                result += other

    return result


def improved_func(limit):
    pass


# 31626
print(initial_func(limit))
# print(improved_func(limit))
