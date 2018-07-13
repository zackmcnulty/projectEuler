#correct!

import eulerFn as efn
import numpy as np

def next_iter():
    n = 2
    a = 5
    b = 3
    c = 9
    d = 7
    while True:
        a += n*8 - 4 #top left
        b += n*8 - 6 # top right
        c += n*8 #bottom right
        d += n*8 - 2  #bottom left
        yield [a, b, c, d]

        n += 1

primes = [3, 5, 7]
notPrimes = [1, 9]
sideLength = 3
diagonal = next_iter()
while len(primes)*9 >= len(notPrimes):
    sideLength += 2
    numSet = diagonal.next()
    for num in numSet:
        if efn.isPrime(num): primes.append(num)
        else: notPrimes.append(num)

print sideLength