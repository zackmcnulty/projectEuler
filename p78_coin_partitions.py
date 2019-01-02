# logic: this question is asking about integer partitions. So it is essentially asking which
# integer can be partitioned in a number of ways divisible by 1 million
# using dynamic programming to save results.

import numpy as np
import time

# Attempt #2
# Use the pentagonal theorem for calculating partition counts, and use
# dynamic programming to simplify this issue. The formula below requires calculating the partitions of n-1, n-2, etc, so
# simply start by calculating partitions for small n and work upwards. Store intermediate results in an array.

# p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + ...
# where the kth term has sign (-1) ** floor(k/2)
# and n is subtracted by the kth general pentagonal number
# see http://mathworld.wolfram.com/PartitionFunctionP.html

# general pentagonal numbers: k(3k-1)/2 for k = 1,-1,2,-2,3,-3,...

def pent_nums():
    fn = lambda k: k*(3*k-1) / 2
    k = 1
    while True:
        yield int(fn(k))
        if k > 0:
            k = -1*k
        else:
            k = 1 + -1*k

# i.e. p(n) = results[n]
size = 100000 
results = [0] * size 
results[0] = 1 # by definition p(0) = 1

n = 1
while results[n-1] % 10**6 != 0:
    gen = pent_nums()
    next_pent = next(gen)
    k = 0
    while n >= next_pent:
        results[n] += ((-1) ** ((k % 4)//2))*results[n - next_pent]
        next_pent = next(gen)
        k += 1
    n += 1

print(results[n-1])
print(n-1)
