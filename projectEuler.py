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

def isPandNum(s):
    if not len(s) == 9:
        return False

    allNums = set([str(x) for x in range(1, 10)])
    sNums = set(s)
    missingNums = allNums.difference(sNums)
    if len(missingNums) == 0:
        return True

    else:
        return False


# 50 Consecutive Prime Sum
#logic: must include an odd number of terms, otherwise it cannot be a prime

primes = filter(lambda x: isPrime(x), [x for x in range(2,10**6)])

for terms in [2*x + 1 for x in range(12, 50)]:
    for i in range(0, 10**6 - terms):
        primeSum = sum(primes[i:i+terms])
        if primeSum in primes:
            print "terms: " + str(terms) + ", " + str(primeSum)

print "done!"

time.sleep(1000)





#48 self powers (correct!)

print sum([x**x for x in range(1,1001)]) % (10**10)

time.sleep(1000)

#46: Goldbach's other Conjecture (correct!)
#logic: move from one odd number to the next. If the number is prime, ignore it. If it is not
# (i.e. if it is composite) look through all prime numbers that are lower than it, and check
# if (n - prime)/2 can produce a square number. If no prime works, you've found your number!

primes = filter(lambda x: isPrime(x), [x for x in range(2,10000)] )

n = 9
foundIt = False
while not foundIt:
    if not n in primes:
        i = 0
        noNum = True
        while primes[i] < n:
            if math.sqrt((n - primes[i])/2).is_integer():
                noNum = False
            i += 1
        if noNum:
            print n
            foundIt = True
    n += 2


time.sleep(1000)





#45: pentagonal, trigonal, and hexagonal numbers
# Logic:Since the hexagonal numbers increase faster, if we loop through every hexagonal number and
# check if it is tri/pent, we have less numbers to check. Solving Pn, Tn for n, we can
# find formulas to see if a number is pentagonal or triagonal (the n given should be an integer)
start = time.time()

def hexNum():
    n = 1
    while True:
        yield n*(2*n - 1)
        n += 1

def isPent(n):
    return ((math.sqrt(24*n + 1) + 1) % 6) == 0

def isTri(n):
    return ((math.sqrt(8*n + 1) - 1) % 2) == 0

for next in hexNum():
    if isPent(next) and isTri(next) and next > 40755:
        print next
        break

end = time.time()
print end - start

time.sleep(1000)



# 44: Pentagon numbers

#logic: given the formula for a pentagon number, we can check if any number is pentagon just
# by solving for n. If n is a natural number, the number is pentagon. Else it is not.
# This will allow us to quickly check if numbers are pentagon
start = time.time()

pNums = set(n*(3*n-1)/2 for n in range(1, 2400))
#def isPent(pn):
    #n = math.sqrt((2.0/3.0)*pn + 1.0/36.0) + 1.0/6.0
    #return abs(n - round(n)) < 0.001

possible = set([])

for j,k in itl.combinations(pNums, 2):
    if j+k in pNums and abs(j-k) in pNums:
        possible.add(abs(j-k))

print min(possible)


end = time.time()
print end - start
time.sleep(1000)


#43 : substring divisibilty (correct!)

def coolSubs(s):
    start = 2
    end = 4
    divs = [2,3,5,7,11,13,17]
    for i in range(0,7):
        if int(s[start + i - 1: end + i]) % divs[i] != 0: return False
    return True

coolNums = set([])

nums = itl.permutations([x for x in range(0,10)])

for pat in nums:
    s = ""
    for i in pat: s += str(i)
    if coolSubs(s) and s[0] != "0":  coolNums.add(int(s))

print coolNums
print sum(coolNums)

time.sleep(1000)

#41 pandigital primes (correct!)

max = 0

for n in range(1,10):
    nums = itl.permutations([x for x in range(1,n+1)])

    for pat in nums:
        s = ""
        for i in pat: s += str(i)
        num = int(s)
        if isPrime(num) and num > max: max = num

print max

time.sleep(1000)



# 39 Champernownes Constant (correct!)

#logic; for 1 digit numbers, there are 9 such numbers (thus 9 digits), for 2 digit numbers,
# there are 9*10 such numbers ( and thus 2*9*10 such digits),
# for 3 digit numbers, there are 9*10*10 (and thus 3*9*10*10 such digits)...
# use this pattern to figure out where the number lies.
# first step, I try to figure out how many digits the number has.
# Then once I know that, I have reduced my n value such that it represents the place of
# the digit of interest when considering only numbers with the determined number of digits.
# So if it was found there are 4 digits, and n = 121, since each number has 4 digits I know I need to look
# at the 31st number. From there, I can subtract 30*4 and see I want the first digit of the 31st number.


def dn(n):
    digits = 1
    while n > 0:
        subtract = digits*9*(10**(digits - 1))
        n -= subtract
        digits += 1
    digits -= 1
    n += subtract

    numOfInterest = 10**(digits-1) + (n-1)/digits
    return str(numOfInterest)[n%digits - 1]

nVals = [10**x for x in range(0, 7)]

prod = 1
for n in nVals:
    prod *= int(dn(n))

print prod


time.sleep(1000)


# 38 pandigital multiples (correct!)
# as n > 1, we have at least two numbers being concatinated. This means each number has to be at most 5 digits.
# ( we have 9 digits total, so its possible x * 1 = 4 digits and x*2 = 5 digits. But this implies
# x is at most 4 digits.
max = 0

for x in range(1, 10000):
    s = ""
    n = 1
    while len(s) < 9:
        s += str(x*n)
        n += 1
    if isPandNum(s) and int(s) > max: max = int(s)

print max


time.sleep(1000)


# 36: double base palindromes (correct!)
def isPal(s):
    n = len(s)
    left = s[:(n+1)/2]
    right = s[n/2:]
    return left == right[::-1]

coolPals = set([])

for num in range(1,10**6):
    binary = str(bin(num))[2:]
    if isPal(str(num)) and isPal(binary): coolPals.add(num)

print sum(coolPals)



time.sleep(1000)


#32 pandigital products (Correct!)

def isPandNum(s):
    if not len(s) == 9:
        return False

    allNums = set([str(x) for x in range(1, 10)])
    sNums = set(s)
    missingNums = allNums.difference(sNums)
    if len(missingNums) == 0:
        return True

    else:
        return False



pandNums = set([])

for i in range(1,1000):
    for j in range(1,10000):
        if isPandNum(str(i) + str(j) + str(i*j)): pandNums.add(i*j)

print pandNums
print sum(pandNums)


time.sleep(1000)

#27 Quadratic Primes (correct!)

#logic:
# as n = 0 has to work, this implies b is prime; narrow down options for b to primes below 1000
# also at n = 1, 1 + a + b is prime; b is odd as it is prime, so a must be odd (otherwise the result cannot be odd)

primes = list([])
for n in range(2,1000):
    if isPrime(n): primes.append(n)



avals = list([2*i + 1 for i in range(-500,500)])

maxCount = 0
maxProd = 0

for b in primes:
    for a in avals:
        fn = lambda n: n**2 + a*n + b
        count = 0
        n = 0
        while isPrime(fn(n)):
            count += 1
            n += 1
        if count > maxCount:
            maxCount = count
            maxProd = a*b

print maxProd


time.sleep(1000)


#624 Two Heads are better than 1 (NOT DONE)


from decimal import *
from fractions import Fraction

#using Binet's formula, we can derive the sum of all these probabilities, and reduce it
# using the formula for a geometric series. We know P(n) = sum (n-1)th prime/2^n based on
# playing with some of the probabilities

def PofN(n):
    val = 1/math.sqrt(5) * (  (2/(1+math.sqrt(5))  *  ((1 + math.sqrt(5)) /4)**n) * (1 / (1 - ((1 + math.sqrt(5))/4)**n))  - 2/(1-math.sqrt(5)) * (((1 - math.sqrt(5)) /4)**n) * (1/ (1 - ((1 - math.sqrt(5))/4)**n)))
    return Fraction(val).limit_denominator(1000000000000000000000000)
#IT FUCKING WORKED! (can handle smaller values. Now just need to find a way to relate them to larger
# so I can calculate P(10**18)
pvals = [PofN(n) for n in range(1,20)]

plt.plot(pvals)
plt.plot(pvals, 'ro')
plt.show()

print "done!"

time.sleep(100)



nthFib = lambda n:int((((1+ math.sqrt(5))**(n-1))-((1 - math.sqrt(5))**(n-1)))/((2**(n-1))* math.sqrt(5))) # Binets Formula: gives nth fib number (if n is large)
# returns fib of (n+1) position

calcProb = lambda mult, maxN: sum([Decimal(nthFib(mult*i))/Decimal((2**(i*mult))) for i in range(1,maxN+1)])

for n in range(1,10): print nthFib(n)

pCount = calcProb(2,100)
P = Fraction(pCount).limit_denominator(1000000000)
print pCount
#P5 = 97/671
#P10 = 633/16775

time.sleep(100)


# yeilds the probability we stop flipping (i.e. we get two heads) at flip numbers that are
# multiples of mult, up to a max number of flips maxN
def flipProbs(maxN, mult):
    # dont need : yield 0
    cur = 1
    last = 0
    fibCount = 2
    while fibCount < maxN:
        if fibCount % mult == 0:
            yield Decimal(cur)/Decimal(2**fibCount)
        temp = cur
        cur = cur + last
        last = temp
        fibCount += 1

sum = 0
for prob in flipProbs(10**36,10**18): # very accurate....
    sum += prob

print sum

time.sleep(100)




def findEndSeq(n, counts, curLevel):
    findHelp(n, counts, 1, True)
    findHelp(n, counts, 1, False)

def findHelp(n, counts, curLevel, lastIsHeads):
    if curLevel < n:
        if lastIsHeads:
            counts[curLevel] += 1
            findHelp(n, counts, curLevel + 1, False)
        else:
            findHelp(n, counts, curLevel + 1, True)
            findHelp(n, counts, curLevel + 1, False)

n = 20
counts = list([0 for i in range(0,n)])
findEndSeq(n, counts, 0)

print counts
# forms the fibonnaci sequence? dividing by the number of possible outcomes at each
# number of coin flips (1 + index of entry in counts; outcomes = 2^ # flips)
# we see this sequence is actually 1/2 of a very common sequence. Something about
# Binet's formula can be used to calculate a value of sequence?
# can skip the simuation know and just know that the probability of it ending at
# flip n is the (nth fib number)/2^n











time.sleep(1000)

#28 Number Spiral Diagonals (correct)

def numGenerator(maxDim):
    cur = 1
    n = 3
    while n <= maxDim:
        for i in range(0,4): # 4 corners of box
            cur += n - 1
            yield cur
        n += 2

print 1+sum(numGenerator(1001))

time.sleep(1000)



# 37 Truncatable Primes (correct!)


count = 0
truncPrimes = set([])


for next in pp.sieve(): # get the nextPrime Number (sieve is a generator)
    isTrunc = True
    s1 = str(next)
    s2 = str(next)
    while len(s1) >= 1:
        if not isPrime(int(s1)) or not isPrime(int(s2)):
            isTrunc = False
            break
        s1 = s1[0:-1]
        s2 = s2[1:]
    if isTrunc and next > 10:
        count += 1
        truncPrimes.add(next)
    if count == 11: break

print truncPrimes

print "sum: " + str(sum(truncPrimes))

time.sleep(1000)


# 35 CircularPrimes (Correct!)
# logic, find all primes below 1 million. For each prime, check if it is circular...

def isPrime(n):
    for div in range(2, int(n**0.5 + 1)):
        if n % div == 0: return False
    return True

primeSet = set([])
circPrimes = set([])

for num in range(2,10**6):
    if isPrime(num): primeSet.add(num)

for prime in primeSet:
    num = str(prime)
    isCirc = True
    i = 1
    while i < len(num):
        newNum = num[-1] + num[0:-1]
        if not isPrime(int(newNum)):
            isCirc = False
            break
        num = newNum
        i += 1
    if isCirc: circPrimes.add(prime)

print len(circPrimes)






time.sleep(1000)

# 26 Reciprocal Cycles (CORRECT!)
#logic: convert all these decimals into strings, and separate them at the "." decimal point. If the
# right side starts with the left side, we have a repeating sequence. If not, move the
# decimal place forward 1 spot by multiplying by 10 and check again


from decimal import *
decis = 2000
getcontext().prec = decis

maxD = 7
maxPattern = 6


for d in range(10,1000):
    num = Decimal(1) / Decimal(d)
    while num < 0.1: num = num * 10
    for patLength in range(1, decis/2):
        numStr = str(num*10**patLength)
        parts = numStr.split(".")
        if len(parts) > 1 and parts[1].startswith(parts[0]):
            if patLength > maxPattern:
                maxPattern = patLength
                maxD = d
            break

print maxD
print maxPattern

time.sleep(1000)




# 30: Digit Fifth Powers (correct!)

totalSum = 0
for num in range(2,10**6):
    digits = str(num)
    sum = 0
    for next in digits:
        sum += int(next)**5
    if sum == num: totalSum += num

print totalSum

time.sleep(1000)


# 29 Distinct Powers (correct!)
# logic; just use a set it will eliminate all duplicates

distinctPowers = set([])
for a in range(2,101):
    for b in range(2,101):
        distinctPowers.add(a**b)

print len(distinctPowers)

time.sleep(1000)



# 205 Dice Game (CORRECT!!!!!!!!!!)
# Logic: first I will generate lists of all possible sums, with duplicates, and then sort them for each person
# next I will traverse the two lists simultaneously, starting at index 0 for pete. I will move down colins
# list as long as Pete's sum is greater, and add this to the counts of outcomes where pete "wins"
# when I reach a point where pete's sum is less, step forward, and start the number of winning counts for
# this next peteSum at the max of the previous (since the list is ascending, we know this sum is greater
# than all the sums of colins that the previous pete sum was).


peteSums = list([])
colinSums = list([])

def rollDice(left, max, curSum, sums):
    if left == 0: sums.append(curSum)
    else:
        for roll in range(1,max + 1):
            rollDice(left - 1, max, curSum + roll, sums)

rollDice(9, 4, 0, peteSums)
rollDice(6,6, 0, colinSums)

peteSums.sort()
colinSums.sort()

totalPete = len(peteSums)
totalColin = len(colinSums)


possibleOutcomes = totalColin * totalPete

peteI = 0
colI = 0
outcomesPeteWins = 0  # number of outcomes where pete wins
curCount = 0 # number of outcomes pete wins for this current index

# We now have two ascending lists representing all the possible sums. For each of Pete's possible
# outcomes, we need to find the number of colin's outcomes it beats! To do so, we do a dual list traversal
# I start at beginning of both lists. If pete > col, pete wins that outcome! Add that to the curCount of wins.
# and look at next num in colin's list. Continue until pete reaches a point where he loses (or draws).
# then move pete forward. As the next number in petes list is >= the last one, we know it would have won
# in all the outcomes where the last one won, so instead of reseting current count and starting at beginning
# of collin's list, we can just let this new number start with the same number of wins as the previous, and
# move forward from there!
while peteI < totalPete and colI < totalColin:
    if peteSums[peteI] > colinSums[colI]:
        curCount += 1
        colI += 1
    else:
        outcomesPeteWins += curCount
        peteI += 1

# fence posting
if not peteI == len(peteSums) - 1: #reached end of colin's list first
    for ind in range(peteI, totalPete): outcomesPeteWins += curCount
    #if we stopped before reaching end of pete's list, all elements from the current one in Pete's
    # list are greater than the entirety of Colins list. Thus add all of colins list


#now we have the number of outcomes where Pete wins! Divide by total number of possible outcomes
print (1.0*outcomesPeteWins)/possibleOutcomes

time.sleep(1000)







# 31 Coin Sums (correct!)
    # we will use recursive backtracking to find every working combination

def findCoinSum(left, coinValues, index):
    if index == 7: return 1
    denom = coinValues[index]
    sum = 0
    for i in range(0, left/denom + 1):
        sum += findCoinSum(left - i*denom, coinValues, index + 1)
    return sum


coinValues = list([200,100,50,20,10,5,2,1])
print findCoinSum(200, coinValues, 0)

time.sleep(1000)

# 33 Digit Cancelling fractions (correct!)
    # logic: for the digits to "cancel" numerator and denominator must have a common digit.
    # Ignore 0 as a possible common digit (leads to trivial case)
    # for digits 1-9, check all possibilities with number in first position
    # i.e. 1x/1y, then 1x/y1, then x1/1y then x1/y1 (last case not possible?)
prod = 1

for i in range(1,10):
    for x in range(1,10):
        for y in range(1,10):
            num1 = (10.0*i + x)/(10.0*i + y)
            num2 = (10.0 * x + i) / (10.0* i + y)
            num3 = (10.0*x + i)/(10.0*y + i)
            num4 = (10*i + x)/(10.0*y + i)
            for num in [num1, num2, num3, num4]:
                if num == 1.0*x/y and num < 1:
                   prod*= num

print prod
print "done"
time.sleep(1000)

# 25: 1000-digit fibonacci number (correct!)

def fib():
    last = 0
    cur = 1
    while True:
        yield cur
        temp = last
        last = cur
        cur = temp + cur

for n, fib in enumerate(fib()):
    if len(str(fib)) >= 1000:
        print "index: " + str(n + 1)
        break

time.sleep(1000)




# 24 Lexicographic Permutations (correct!)
        # figure out how many ways to

def factorial(n):
    if n == 1: return 1
    else: return n*factorial(n-1)

numsLeft = list([0,1,2,3,4,5,6,7,8,9])
curPos = 0
pattern = ""

while not len(numsLeft) == 1:
    n = len(numsLeft)
    index = 0
    perms = factorial(n-1)
    # If we have n items left, there are (n-1)! permutations that have a specific next digit
    # the first perms permutations have the lowest digit remaining at the front,
    # then the next perm permutations have the next lowest digit. So keep moving forward until the
    # position count exceeds 1 million. Then we know we cannot move to the next digit without passing
    # over the combination we want. So we move on to the next digit and repeat.
    while curPos < 10**6:
        curPos += perms
        index += 1
    curPos -= perms
    index -= 1
    pattern += str(numsLeft[index])
    del numsLeft[index]

print pattern + str(numsLeft[0])





time.sleep(1000)





#23: Nonabundant sums (correct!)
#logic: start by finding sum of all divisors of each number up to 28123. Then find all abundant nums

divSums = {}

def findDivSum(n):
    sum = 0
    for div in range(1, n/2 +1):
        if n % div == 0: sum += div
    return sum

for num in range(1,28124):
    divSums[num] = findDivSum(num)

abunNums = list([])
for key in divSums:
    if key < divSums[key]: abunNums.append(key)


posSums = set([])
for num1 in abunNums:
    for num2 in abunNums:
        posSums.add(num1 + num2)

sum = 0
for k in range(1,28124):
    if not k in posSums: sum += k

print sum

time.sleep(1000)





#22: Name Scores (Correct!)

def nameVal(name):
    val = 0
    for letter in name: val += ord(letter) - 64
    return val



with(open("p022_names.txt")) as inputFile:
    for line in inputFile:
        line = line.replace("\"", "")
        names = line.split(",")
        names.sort()

    sum = 0
    for i in range(len(names)):
        sum += nameVal(names[i])*(i+1)

print sum

time.sleep(1000)

#21 Amicable Numbers (correct!)

divSums = {}

def divisorSum(n):
    sum = 0
    for div in range(1, n/2 +1):
        if n % div == 0: sum += div
    return sum

for num in range(1,10000):
    divSums[num] = divisorSum(num)


sumOfAmicable = 0
for key in divSums:
    if divSums.has_key(divSums[key]) and divSums[divSums[key]] == key and not key == divSums[key]:
        sumOfAmicable += key

print sumOfAmicable

time.sleep(1000)



#17 Number Letter Counts (correct!)

def getCount(num,names):
    if num == 0: return 0
    elif num >= 100:
        topNums = len(names[num/100]) + len(names[100]) #counts for hundreds + "and" + count for lowers
        if num % 100 == 0: return topNums
        else: return topNums + 3 + getCount(num % 100, names)

    elif num >= 20:
        return len(names[num - num % 10]) + getCount(num % 10, names)

    else: return len(names[num])

names = {1: "one", 2: "two", 3:"three", 4:"four", 5:"five", 6:'six', 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16: "sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eigthy", 90:"ninety", 100:"hundred"}
letterCount = 0
for num in range(1,1000):
    letterCount += getCount(num, names)
print letterCount + len("onethousand")



time.sleep(1000)

#4 Largest Palindrome Product (correct!)

def isPalindrome(num):
    s = str(num)
    for i in range(0, len(s)/2):
        if not s[i] == s[-(i+1)]: return False
    return True

maxPal = None
for j in range(100,1000):
    for k in range(100,1000):
        prod = j*k
        if prod > maxPal and isPalindrome(prod): maxPal = prod

print maxPal

time.sleep(1000)

# 3: Largest Prime Factor (Correct!)

def isPrime(num):
    for div in range(2, int(num**0.5)+1):
        if num % div == 0: return False
    return True

maxPrime = 2
for divisor in range(2, int(600851475143**0.5) + 1):

    if 600851475143 % divisor == 0 and isPrime(divisor): maxPrime = divisor

print maxPrime

time.sleep(1000)


#20 Factorial Digit Sum (correct!)

def factorial(n):
    if n == 1: return 1
    else: return n*factorial(n-1)

num = factorial(100)
s = str(num)

sum = 0
for digit in s: sum += int(digit)

print sum


time.sleep(1000)

# 14: Highly Divisible Triangle Numbers (correct!)

def nextTri():
    n = 1
    triNum = 0
    while True:
        triNum += n
        n += 1
        yield triNum

def countFacts(n):
    count = 0
    for facts in range(1, int(n**0.5) + 1):
        if n % facts == 0: count += 2 # double counts square numbers.
    return count

for num in nextTri():
    if countFacts(num) > 500:
        print num
        break


time.sleep(1000)

# 14 Longest Collatz Sequence (correct!)
def ColSeq(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + ColSeq(n/2)
    else:
        return 1 + ColSeq(3*n + 1)

maxLength = 0
bestNum = 0
for n in range(1, 10**6):
    nextLength = ColSeq(n)
    if nextLength > maxLength:
        maxLength = nextLength
        bestNum = n


print bestNum

time.sleep(1000)

#7 10001st prime (correct!):
def isPrime(n):
    for facts in range(2, int(n**0.5) + 1):
        if n % facts == 0: return False
    return True

count = 1
num = 1
while count < 10001:
    num += 2
    if isPrime(num):
        count += 1
print num




#10: Sum of Primes (correct!)
# logic: brute force; check all possible numbers as factors up to sqrt(n)

def isPrime(n):
    for facts in range(2, int(n**0.5) + 1):
        if n % facts == 0: return False
    return True

sum = 0
for n in range(2, 2*(10**6)):
    if isPrime(n):
        sum += n


print sum
time.sleep(1000)


#19: Counting Sundays (correct!)
# logic: assign a number to each day of week, 0 = sunday, 1 = mon, 2 = tues, etc
# each month, add the number of days then modulo 7 to figure out what day it is
day = 1

count = 0;
for year in range(1900, 2001):
    for month in range(1,13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day += 31
        elif month == 2:
            if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
                day += 29
            else:
                day += 28
        else:
            day += 30
        if year > 1900 and day % 7 == 0: count += 1

print count

time.sleep(1000)



#8: largest product in a series (correct!)
#logic: if I take the product of the first 13. Then I can simply parse through all possible products by
# dividing out the first number and multiplying on the 14 to get the product of the next 13 nums
# just be careful about division by zero. Also not that if a zero was in the previous product it fucks things up

seq = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
seq = str(seq)
maxProd= 1
for i in range(0,13):  # get sum of first 13 nums
    maxProd *= int(seq[i])

curProd = maxProd

for i in range(13, len(seq)):
    if not int(seq[i -13]) == 0:
        curProd = (curProd)*int(seq[i])/int(seq[i - 13])
    else: # cant divide by zero so we have to recalculate the new product
        curProd = 1
        for k in range(i-12, i + 1):
            curProd *= int(seq[k])
    if curProd > maxProd: maxProd = curProd

print maxProd
time.sleep(1000)


#16: Power digit sum (correct)
num = str(2**1000)
sum = 0
for digit in num:
    sum += int(digit)
print sum


time.sleep(1000)



# 13: large sum (Correct)
with(open('50digitnums.txt')) as inputFile:
    sum = 0
    for line in inputFile:
        sum += int(line)
    s = str(sum)
    print s[0:10]



time.sleep(1000)

# 42: Coded Triangle Numbers (correct!)
relevantTris = []

tri = lambda n: (n+1)*n/2
for n in range(1,50): relevantTris.append(tri(n))

print relevantTris

with(open('p042_words.txt')) as inputFile:
    count = 0
    for line in inputFile:
        list = line.strip().replace("\"", "")
        words = list.split(",")

    for w in words:
        letterSum = 0
        for letter in w:
            letterSum += ord(letter) - 64
        if letterSum in relevantTris: count += 1

print count
time.sleep(1000)

# 107: triangle containment (CORRECT! 15% difficulty!!!!!)
#logic: if the origin is within, lines to the origin from each vertex separate triangle into three parts
# which sum to the overall triangle area. Using the fact that Area triangle = 1/2||AB x AC||, we can see these
# sub triangles are made up of the vectors AO, BO, CO where O is the origin. They then have areas 1/2||AO x BO|| etc
with(open('p102_triangles.txt')) as inputFile:
    count = 0
    for line in inputFile:
        line = line.strip()
        points = line.split(",")
        A = [int(points[0]), int(points[1])]
        B = [int(points[2]), int(points[3])]
        C = [int(points[4]), int(points[5])]
        # in two dimensions, cross product is easy ||[a b 0] x [c d 0]|| = absolute(ad - bc)

        vectAB = np.subtract(B,A)
        vectAC = np.subtract(C,A)

        #works!
        trueArea = 0.5*np.absolute(vectAB[0]*vectAC[1] - vectAB[1]*vectAC[0])

        # AO x BO
        subArea1 = 0.5*np.absolute(A[0]*B[1] -A[1]*B[0])

        # AO x CO
        subArea2 = 0.5*np.absolute(A[0]*C[1] - A[1]*C[0])

        # BO x CO
        subArea3 = 0.5*np.absolute(B[0]*C[1] - B[1]*C[0])

        if trueArea == subArea1 + subArea2 + subArea3: count += 1
print count



time.sleep(1000)

#67: max path sum (CORRECT!)
# same logic as #18 below, but automated to run of txt file of nums
results = []
with(open('p067_triangle.txt')) as inputFile:
    for line in inputFile:
        line = line.strip()
        results.append(list(line.split(" ")))
lastRow = results[-1]
curRow = -2
aboveRow = results[curRow]
while len(aboveRow) > 1:
    for i, val in enumerate(aboveRow):
        aboveRow[i] = int(val) + max(int(lastRow[i]), int(lastRow[i + 1]))
    lastRow = aboveRow
    curRow -= 1
    aboveRow = results[curRow]
maxPath = int(results[0][0]) + max(int(lastRow[0]), int(lastRow[1]))
print maxPath
time.sleep(1000)


#18: max path sum (CORRECT!)
#start at second to last row; Set each entry to be its value + max of values below it;
# move up one row and repeat process.
rowBelow = list([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])
while True:
    nextRow = list(input("Next Row?: "))
    for i, val in enumerate(nextRow): # i = index, val = current val in that index
        nextRow[i] = val + max(rowBelow[i], rowBelow[i + 1])
    print nextRow
    rowBelow = nextRow






time.sleep(1000)

# 15 Lattice Paths (correct!)

#solved without code: try thinking of the fact that you have 40 moves to make, 20 rights and 20 downs.
# so you have 40 slots to fill, 20 with rights and the rest with downs. There are 40 choose 20 ways to fill
# those first 20 slots, and the rest are just filled with downs.

def countPaths(N):
    downsLeft = N
    rightsLeft = N
    print countHelp(downsLeft, rightsLeft)

def countHelp(downs, rights):
    if downs == 0 or rights == 0: return 1
    else:
        return countHelp(downs - 1, rights) + countHelp(downs, rights - 1)

for n in range(1,21):
    countPaths(n)

time.sleep(1000)


# 357 Prime Generating integers
    # n cannot be divisible by 4 (then it would be divisible by 2 but 2 + n/2 would be even)
    # n cannot be odd: n cannot be product of odd numbers;
        #if ab = n for odd a,b, then a + n/a= a + b = sum of two odds = even (not prime)
    # n cannot be square: if n = a^2 then a + n/a = a + a = 2a is even and thus not prime
    # n cannot be 2*square?????
    #n cannot be the product of two even numbers (same as cannot be divisible by 4)

    # i.e. n is the product of 1 even number x and 1 odd number y such that x + n/x is prime and y + n/y
        # i.e. x + y is prime
        # note: as 1, n are factors of n this implies that n + 1 is prime. i.e. n is one less than a prime
            # most numbers 1 less than prime satisfy this (besides 18,66 because 6 + 3 = 9)
            #satisfy this property

        # every even number > 2 can be written as sum of two primes
            #p1 + p2 = e :  so d + n/d = d + (p1 + p2)/d. Choose d = p2: p2 + 1 + p1/p2????

        # search through all possible values of x and y such that xy < 100000000. If I find a none prime, cross it off the list!






# 8 largest product in a series

series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

for i in enumerate(series):
    if series[i] == 0:
        series = series[0:i-12] + series[i+12]






#34 (Correct!)
def factorial(n):
    if n == 0: return 1
    else: return n*factorial(n-1)

facts = []
for k in range(0,10): facts.append(factorial(k))

#facts[i] = i!

# no 1 digit nums
# 2 digit nums only include 0-4
# 3 digit nums only include 0-6
# 4 digit nums only include 0-7
# 5 digit nums only include 0-8

nums = list([])
for k in range(0, 9999999):
    sum = 0
    n = k
    string = str(k)
    for i in range(0,len(string)):
        sum += facts[int(string[i])]
    if sum == k: print k
print "done!"
time.sleep(1000)




# Problem 39: Integer right triangles (CORRECT)

# a + b + c <= 1000
# a = st, b = (s^2 - t^2)/2, c = (s^2 + t^2)/2
# all triples: m(2k+1)(k+n+1) <= 500 for k>n>=0 and m > 0


def getP(m, k, n):
    return m*(2*k + 1)*2*(k+n+1)

myRims = dict([])

m = 1
k = 1
n = 0
while (2*k + 1)*(k+1) <= 500:
    for n in range(0, k):
        nextP = getP(m,k,n)
        if nextP > 1000: break
        elif myRims.has_key(nextP):
            myRims[nextP] += 1
        else:
            myRims[nextP] = 1
    k += 1

newTerms = dict([])
for keys in myRims:
    m = 2
    while m*keys <= 1000:
        if newTerms.has_key(m*keys):
            newTerms[m*keys] +=1
        else:
            newTerms[m*keys] = 1
        m += 1

for key in newTerms:
    if myRims.has_key(key): myRims[key] += newTerms[key]
    else: myRims[key] = newTerms[key]

max = 0
bestKey = 0

for key in myRims:
    if myRims[key] > max:
        max = myRims[key]
        bestKey = key

print(str(bestKey) + ", " + str(max))
time.sleep(1000)


# 49 Prime Permutations (correct!)
# only way for this to work is if 1 number >= 7, one is <=3

# first num < 3340
# the numbers will cycle, and thus each spot takes on each number
    # NO zero. we can have 1,4,8 or 1,8,5
# 185x -> 518x ->851x nope
# 296x -> 629x -> 962x   x= 9






time.sleep(1000)





#3 smallest multiple (correct!)

# numbers that matter 20, 19, 18, 17, 16,15,14,13,12,11, (others are factors of these anyways)
# 10 9 8 7 6
current = 20
notDone = True
while notDone:
    for k in range(11,20):
        if not current % k == 0:
            current += 20
            break
        elif k == 19: notDone = False

print current



#2 Even Fib Numbers (CORRECT!)

# I noticed that the even fib numbers are related by En = 4*En-1 + En-2

evens = list([2,8])
index = 2
next = 0
while next < 4*10**6:
    next = 4*evens[index - 1] + evens[index - 2]
    if next < 4*10**6:
        evens.append(next)
        index +=1

print(sum(evens))






from fractions import gcd

sum = 0
known = dict([])
for k in range(1,2*10**6 + 1):
    x = 1
    y = k**3
    while not y == 1:
        gcf = gcd(x,y)
        if gcf == 1:
            x += 1
            y -= 1
        else:
            x = x/gcf
            y = y/gcf
            if x == 1 and y in known:
                x = known[y]
                break
    known[k] = x
    sum += x

print sum


