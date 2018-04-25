#!/usr/bin/env python
"""Practice"""
# 87   + 78   = 165
# 165  + 561  = 726
# 726  + 627  = 1353
# 1353 + 3531 = 4884


def reverse(s):
    """reverse"""
    return s[::-1]


def isPal(s):
    """isPal"""
    rev = reverse(s)

    if s == rev:
        return True
    return False


# my data ARR is seed value to iterate to Palindromic number

ARR = 87
MYPAL = isPal(str(ARR))
print "starting value is = ", ARR

while MYPAL != 1:
    ARR = ARR + int(reverse(str(ARR)))
    print "continue to iterate", ARR
    MYPAL = isPal(str(ARR))

print "My Palindromic number is: ", ARR
