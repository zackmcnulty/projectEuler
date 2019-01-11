  
~ def isPrime(n):
~     if n <= 1: return False
~     if n == 2: return True
~     for div in range(2, int(n**0.5 + 1)):
~         if n % div == 0: return False
~_    return True
  
  #46: Goldbach's other Conjecture (correct!)
  #logic: move from one odd number to the next. If the number is prime, ignore i>
  # (i.e. if it is composite) look through all prime numbers that are lower than>
  # if (n - prime)/2 can produce a square number. If no prime works, you've foun>
  
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
