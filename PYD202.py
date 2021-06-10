# TODO
n = eval(input())
if n % 3 == 0:
    if n % 5 == 0:
        print('%d is a multiple of 3 and 5.' %n)
    else:
        print('%d is a multiple of 3.' %n)
elif n % 5 == 0:
    print('%d is a multiple of 5.'%n)
else:
    print('%d is not a multiple of 3 or 5.' %n)



"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""