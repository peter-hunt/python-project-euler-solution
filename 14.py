"""
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

limit = 1_000_000


def initial_solve(limit):
    cache = {1: 0}

    def collatz(num):
        nonlocal cache

        if num not in cache:
            cache[num] = collatz(num // 2 if num % 2 == 0 else num * 3 + 1) + 1

        return cache[num]

    result = 1
    maximum = 0

    for num in range(2, limit):
        if collatz(num) > maximum:
            result = num
            maximum = collatz(num)

    return result


def improved_solve(limit):
    cache = {1: 0}

    def collatz(num):
        nonlocal cache

        if num not in cache:
            if num % 2 == 1:
                cache[num] = collatz(num * 3 + 1) + 1
            else:
                twos = 1
                num //= 2
                while num % 2 == 0:
                    twos += 1
                    num //= 2

                odd = collatz(num)
                for i in range(1, twos + 1):
                    cache[num * 2 ** i] = odd + i

        return cache[num]

    result = 1
    maximum = 0

    for num in range(limit // 2, limit):
        if collatz(num) > maximum:
            result = num
            maximum = collatz(num)

    return result


# 837799
print(initial_solve(limit))
print(improved_solve(limit))
