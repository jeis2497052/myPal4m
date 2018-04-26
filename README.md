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

# And just a little more fun with this code

```sh
./mypal.py
starting value is =  89
continue to iterate 187
continue to iterate 968
continue to iterate 1837
continue to iterate 9218
continue to iterate 17347
continue to iterate 91718
continue to iterate 173437
continue to iterate 907808
continue to iterate 1716517
continue to iterate 8872688
continue to iterate 17735476
continue to iterate 85189247
continue to iterate 159487405
continue to iterate 664272356
continue to iterate 1317544822
continue to iterate 3602001953
continue to iterate 7193004016
continue to iterate 13297007933
continue to iterate 47267087164
continue to iterate 93445163438
continue to iterate 176881317877
continue to iterate 955594506548
continue to iterate 1801200002107
continue to iterate 8813200023188
My Palindromic number is:  8813200023188
```
# Try big numbers like starting value is =  1186060307891929990

```sh
./mypal.py
starting value is =  1186060307891929990
continue to iterate 2185352294922536801
continue to iterate 3271704589845072613
continue to iterate 6434410079699144336
.
.
.
My Palindromic number is:  44562665878976437622437848976653870388884783662598425855963436955852489526638748888307835667984873422673467987856626544

```



# References:

[REVERSAL-ADDITION PALINDROME TEST ](http://jasondoucette.com/pal/1186060307891929990)

[Palindromic Number](https://en.wikipedia.org/wiki/Palindromic_number)
