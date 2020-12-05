"""
Counting Sundays

You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date


def initial_solve():
    result = 0
    weekday = 1

    for year in range(1900, 2001):
        if year % 4 == 0 and year % 100 != 0:
            months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if year == 2000:
            months = months[:-1]

        for month in months:
            weekday = (weekday + month) % 7
            if weekday == 0 and year != 1900:
                result += 1

    return result


def improved_solve():
    result = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:
                result += 1

    return result


# 171
print(initial_solve())
print(improved_solve())
