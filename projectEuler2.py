import numpy as np
import time
import matplotlib.pylab as plt
import math
import itertools as itl



import pyprimes as pp
## myPrimes = pp.erat(10**6)
## print len(myPrimes)
def isPrime(n):
    if n <= 1: return False
    if n == 2: return True
    for div in range(2, int(n**0.5 + 1)):
        if n % div == 0: return False
    return True

#51: Prime Digit Replacement
#logic:
    # the final digit cannot be replaced, as if the family includes 8 different members this implies
    # the position which varies must take on even digits. This would make the number not prime
    # if the final digit was variable
    # digits replaced < total digits
        # if there is only one fixed number, it must be the last one (see above
        # the pattern will be divisible by 11..11 if when the numbers match the fixed number
        # (i.e. if we have ****3, then 33333/11111 = 3 not prime) and zero cant be the leading digit
    # If first digit is variable, 0 is the one value it does not take on

#for now, assume the number is between 100,000 and 1 million (has 6 digits)
import regex

#first attempt
primes = filter(lambda x: isPrime(x), [x for x in range(10**5,10**6)])

def matchesPattern(s, pat):
    s = list(s)
    pat = list(pat)
    numSet = set([])
    for i in range(0, len(pat)):
        next = pat[i]
        if next == "i":
            numSet.add(s[i])
    return len(numSet) == 1


def expandPattern(pats,index, currentPattern):
    if index < 6:
        expandPattern(pats, index + 1, currentPattern)

        newSet = set([])
        oldPattern = currentPattern
        newPattern = list(currentPattern)
        newPattern[index] = "i"
        for p in pats[oldPattern]:
            if matchesPattern(str(p), newPattern): newSet.add(p)
        pats["".join(newPattern)] = newSet

        expandPattern(pats, index + 1, "".join(newPattern))

pats = {"******": primes}
currentPat = "******"

expandPattern(pats, 0, currentPat)

#so far, the primes are correctly sorted into their matching patterns. The only issue is that
# each group is not guarenteed to have same other numbers.

for pattern in pats.keys():
    print( pattern, pats[pattern])



print ("done!")














# second try
primes = filter(lambda x: isPrime(x), [x for x in range(10**5,10**6)])

def makePatSet(letPats, index, currentPattern):
     if index < 6:
         makePatSet(letPats, index + 1, currentPattern)

         newPattern = list(currentPattern)
         newPattern[index] = "i"
         newPattern = "".join(newPattern)
         letPats.add(newPattern)

         makePatSet(letPats, index + 1, newPattern)

letPats = set()
options = set()

makePatSet(letPats, 0, "******")

for pat in letPats:
    for k in range(0,10):
        newPat = ""
        for letter in pat:
            if letter == "i":
                newPat += str(k)
            else:
                newPat += "*"
        options.add(newPat)

def matchesPattern(s, pat):
    s = list(s)
    pat = list(pat)
    for i in range(0, len(s)):
        if s[i] != pat[i] and pat[i] == "i":
            return False;
    return True

for pattern in options:
    matchingPrimes = set()
    for p in primes:
        if matchesPattern(str(p), pattern):
            matchingPrimes.add(p)
    if len(matchingPrimes) == 8:
        print (matchingPrimes)
        break

print ("done!")

















