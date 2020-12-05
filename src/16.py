"""
Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

exponent = 1000


def initial_func(exponent):
    return sum(int(digit) for digit in f'{2 ** exponent}')


def improved_func(exponent):
    pass


# 1366
print(initial_func(exponent))
# print(improved_func(exponent))
