
  #27 Quadratic Primes (correct!)
  
  #logic:
  # as n = 0 has to work, this implies b is prime; narrow down options for b to >
  # also at n = 1, 1 + a + b is prime; b is odd as it is prime, so a must be odd>
def isPrime(n):
     if n <= 1: return False
     if n == 2: return True
     for div in range(2, int(n**0.5 + 1)):
        if n % div == 0: return False
     return True
  
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
