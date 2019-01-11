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
