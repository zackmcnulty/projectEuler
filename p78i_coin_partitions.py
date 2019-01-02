# logic: this question is asking about integer partitions. So it is essentially asking which
# integer can be partitioned in a number of ways divisible by 1 million
# using dynamic programming to save results.

import numpy as np
import time

size = 10**6

# we store n on the vertical direction, m in the horizontal.
results = np.ones((size,size))
results *= -1
results = results.astype(int)

#print(results)
#time.sleep(10)

# calculating partitions

# start at n
# then choose the first part size;
# for all sizes i from 1 to n
#   first part is size i   
#   the rest/other parts  must be a partition
#   of n - i into pieces at most size i
"""
def calc_partitions(n):
    calc_partitions_helper(n,n)
    return results[n,n]


# partition n into parts at most m


def calc_partitions_helper(n,m):
    if n < m:
        if results[n,n] == -1: calc_partitions_helper(n,n)
        results[n,m] = results[n,n]
    elif m == 0:
        results[n,m] = 0
    elif n <= 1 or m == 1:
        results[n,m] = 1

    else:
        if results[n-m, m] == -1: calc_partitions_helper(n-m, m)
        if results[n, m-1] == -1: calc_partitions_helper(n, m-1)
        results[n,m] = results[n, m-1] + results[n-m, m]


N = 1 

while calc_partitions(N) % (10**6) != 0:
    print(results[N,N])
    N += 1


print(N)
"""


# Attempt #2
