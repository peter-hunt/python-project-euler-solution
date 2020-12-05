"""
Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 1_000_000


def initial_func(numbers, index):
    def perm(numbers):
        if len(numbers) == 1:
            yield [numbers[0]]
        else:
            for number in sorted(numbers):
                others = [*numbers]
                others.remove(number)
                for choice in perm(others):
                    yield [number, *choice]

    return [*perm(numbers)][index - 1]


def improved_func(numbers, index):
    pass


# 2783915460
print(initial_func(numbers, index))
# print(improved_func(numbers, index))
