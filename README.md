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


```
# Results using seed of 87

```sh
./mypal.py
starting value is =  87
continue to iterate 165
continue to iterate 726
continue to iterate 1353
continue to iterate 4884
My Palindromic number is:  4884
```



# References:

[REVERSAL-ADDITION PALINDROME TEST ](http://jasondoucette.com/pal/1186060307891929990)

[Palindromic Number](https://en.wikipedia.org/wiki/Palindromic_number)
