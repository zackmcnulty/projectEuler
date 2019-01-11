# 50 Consecutive Prime Sum
#logic: must include an odd number of terms, otherwise it cannot be a prime

def isPrime(n):
    if n <= 1: return False
    if n == 2: return True
    for div in range(2, int(n**0.5 + 1)):
        if n % div == 0: return False
    return True


primes = filter(lambda x: isPrime(x), [x for x in range(2,10**6)])

for terms in [2*x + 1 for x in range(12, 50)]:
    for i in range(0, 10**6 - terms):
        primeSum = sum(primes[i:i+terms])
        if primeSum in primes:
            print "terms: " + str(terms) + ", " + str(primeSum)

print ("done!")

