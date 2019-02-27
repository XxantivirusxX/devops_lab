import random


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
year = random.randint(1, 2200)
print(is_leap(year))
