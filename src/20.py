"""
Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

limit = 100


def initial_solve(limit):
    def factorial(n):
        if n < 2:
            return 1

        return factorial(n - 1) * n

    return sum(int(digit) for digit in f'{factorial(limit)}')


def improved_solve(limit):
    def fake_factorial(n):
        if n < 2:
            return 1

        if n % 10 == 0:
            shortened = n
            while shortened % 10 == 0:
                shortened //= 10

            return fake_factorial(n - 1) * shortened
        else:
            return fake_factorial(n - 1) * n

    return sum(int(digit) for digit in f'{fake_factorial(limit)}')


# answer
print(initial_solve(limit))
print(improved_solve(limit))
