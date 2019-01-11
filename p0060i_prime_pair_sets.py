# logic: 

max_n = 100000
primes = set([2])

for n in range(3, max_n + 1):
    for div in primes:
        if n % div == 0:
            break
    else:
        primes.add(n)




