# myPal4m - quick test for Palindromic numbers

```python

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
    rev = reverse(s)

    if ( s == rev ):
        return True
    return False


# my data
#ARR = [87, 165, 726, 1353]
ARR = 87
mypal = isPal(str(ARR))
print "starting value is = ", ARR

while (mypal != 1):
    ARR = ARR + int(reverse(str(ARR)))
    print "continue to iterate", ARR
    mypal = isPal(str(ARR))

print "My solution is: ", ARR


```
# Results using seed of 87

```sh
starting value is =  87
continue to iterate 165
continue to iterate 726
continue to iterate 1353
continue to iterate 4884
My solution is:  4884
```
