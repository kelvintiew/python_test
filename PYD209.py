import math
x = eval(input())
y = eval(input())

# TODO
distance = math.sqrt((x - 5) ** 2 + (y - 6) ** 2)

if distance <= 15:
    print('Inside')
else:
    print('Outside')



"""
Inside
Outside
"""