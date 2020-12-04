"""
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

limit = 1000

ones_and_teens = [
    0,  # zero isn't spoken
    3,  # one
    3,  # two
    5,  # three
    4,  # four
    4,  # five
    3,  # six
    5,  # seven
    5,  # eight
    4,  # nine
    3,  # ten
    6,  # eleven
    6,  # twelve
    8,  # thirteen
    8,  # fourteen
    7,  # fifteen
    7,  # sixteen
    9,  # seventeen
    8,  # eighteen
    8,  # nineteen
]

tens = [
    0,  # zero isn't spoken
    0,  # ten is used in teens
    6,  # twenty
    6,  # thirty
    5,  # forty
    5,  # fifty
    5,  # sixty
    7,  # seventy
    6,  # eighty
    6,  # ninety
]


def initial_solve(limit):
    def count_letter(num):
        if num < 20:
            return ones_and_teens[num]
        elif num == 1000:
            return 11

        if num % 1000 >= 100:
            hundred = ones_and_teens[num % 1000 // 100] + 7
            if num % 100 != 0:
                hundred += 3
        else:
            hundred = 0

        if num % 100 < 20:
            return hundred + ones_and_teens[num % 100]
        else:
            ten = tens[num % 100 // 10]
            one = ones_and_teens[num % 10]
            return hundred + ten + one
    return sum(count_letter(num) for num in range(1, limit + 1))


def improved_solve(limit):
    pass


# 1366
print(initial_solve(limit))
# print(improved_solve(limit))
