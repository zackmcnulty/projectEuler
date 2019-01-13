# logic: First, note that sum_{i=1} i^2 = n(n+1)(2n+1)/6
# Therefore, we can represent any consecutive sum by n(n+1)(2n+1)/6 - m(m+1)(2m+1)/6
# Since we must have at least  two numbers to make up a sum keep this in mind.
# Also, since we must have at least two numbers in our sum, our sum is
# at least n^2 + (n-1)^2 < 2n^2. This should be less than 10^8, giving us
# some bounds for n: 2n^2 < 10^8 --> sqrt(2)n < 10^4 --> n < 10^4/rt(2)

import time
import math
import itertools as itl

# second approach: find all palindromes first, then check if they could
# be represented by a sum of integers.

# all one digit numbers are palindromes
pals = [1,2,3,4,5,6,7,8,9]

# find pals with even number of digits (i.e. 2 to 8 digits)
for digits in range(2, 10, 2):
    choices = itl.product(list(range(10)), repeat=digits//2)
    for choice in choices:
        # first digit of number cannot be zero
        if not choice[0] == 0:
            s = "".join([str(digit) for digit in choice])
            pals.append(int(s + s[::-1]))

            # now make odd digit pals
            if digits != 8:
                for mid_digit in range(10):
                    pals.append(int(s + str(mid_digit) + s[::-1]))


# Another way to consider this sum of consecutive integers is to consider how many terms it has
# i.e. For a sum with k terms with minimum term n^2, we have:

# sum = sum_{i=1}^{n+k} i^2 - sum_{i=1}^{n}i^2 = (n+k)(n+k+1)(2n+2k+1)/6 - (n)(n+1)(2n+1)/6 
# pal = (n+k)(n+k+1)(2n+2k+1)/6 - (n)(n+1)(2n+1)/6  
# 6*pal = k (2 k^2 + 6 k n + 3 k + 6 n^2 + 6 n + 1)  -> thanks wolfram alpha
# 6*pal / k = 6n^2 + (6k + 6)n + (2k^2 + 3k + 1)

for pal in pals:



time.sleep(100)





# First approach (correct!): find the sum first, then check for palindrome
start = time.time()

def is_pal(n):
    s = str(n)
    size = len(s)//2
    return s[:size] == s[-1:-size-1:-1]

def calc_sum(i):
    return i*(i+1)*(2*i+1) / 6

valid_nums = set([])
for n in range(2,int(10000 / math.sqrt(2))):
    # check larger m values first. When the sum > 10**8
    # no need to check lower m
    # as these include more terms in the sum
    for m in list(range(n-1))[::-1]:

        num = int(calc_sum(n) - calc_sum(m))
        if num >= 10**8: break
        elif is_pal(num) :
            valid_nums.add(num)

print(sum(valid_nums))
print("runtime: ", time.time() - start)
