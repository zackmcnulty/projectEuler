# logic: Firstly, note that there has to be some limitations on which numbers are used as
# the bases. If our number is a^2 + b^3 + c^4, then we know c <= (50 mil) ^ 0.25 ~ 84  
# b <= (50 mill)^(1/3) ~ 368 and a <= (50 mil)^0.5 ~ 7071. These values are reasonably
# small, so simply enumerating all the possibilities seems like a sufficient approach
# First, we will start by generating the relevant primes

import time
import numpy as np
import itertools as itl

start = time.time()

primes = [2]

for num in range(3,7072,2):
    for div in primes:
        if num % div == 0:
            break
    else:
        # no prime divisors. Must be prime
        primes.append(num)

primes = np.asarray(primes)
primes84 = primes[primes <= 84]
primes368 = primes[primes <= 368]

ans = set(filter(lambda x: x <= 50*10**6, map(lambda x: x[0]**2 + x[1]**3 + x[2]**4,  list(itl.product(primes, primes368, primes84)))))
print(len(ans))

print("runtime: ", time.time() - start)
