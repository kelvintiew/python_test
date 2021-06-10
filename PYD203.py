# TODO
year = eval(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('%d is a leap year.' %year)
else:
    print('%d is not a leap year.' %year)


"""
_ is a leap year.
_ is not a leap year.
"""