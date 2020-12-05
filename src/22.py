"""
Names scores

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


content = None  # names.txt
names = eval(f'[{content}]')


def initial_func(names):
    def name_score(name):
        return sum(ord(letter) - 64 for letter in name)

    result = 0

    for index, name in enumerate(sorted(names)):
        result += (index + 1) * name_score(name)

    return result


def improved_func(names):
    pass


# 871198282
print(initial_func(names))
# print(improved_func(names))
