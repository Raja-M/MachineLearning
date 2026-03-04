import sys
# -*- coding: encoding -*-
# -*- coding: cp1252 -*-
print ("Hello, World!")
# python -c for command
# python -m for module
# python -i for interactive
print("Number of arguments:", len(sys.argv))
print("Arguments:", sys.argv)
'''
17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # floored quotient * divisor + remainder

Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

'''
a, b = 1, 2
while a < 10:
    a,b = b, a+b
print(a)
