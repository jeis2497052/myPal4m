#!/usr/bin/env python
"""Practice"""
# 87   + 78   = 165
# 165  + 561  = 726
# 726  + 627  = 1353
# 1353 + 3531 = 4884


def reverse(s2rev):
    """reverse"""
    return s2rev[::-1]


def isPal(s2test):
    """isPal"""
    rev = reverse(s2test)

    if s2test == rev:
        return True
    return False


# my data ARR is seed value to iterate to Palindromic number

ARR = 1186060307891929990
ARR = 89
MYPAL = isPal(str(ARR))
print "starting value is = ", ARR

while MYPAL != 1:
    ARR = ARR + int(reverse(str(ARR)))
    print "continue to iterate", ARR
    MYPAL = isPal(str(ARR))

print "My Palindromic number is: ", ARR
