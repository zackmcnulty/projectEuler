_ # 37 Truncatable Primes (correct!)
  count = 0
  truncPrimes = set([])
  
  
  for next in pp.sieve(): # get the nextPrime Number (sieve is a generator)
      isTrunc = True
      s1 = str(next)
      s2 = str(next)
      while len(s1) >= 1:
          if not isPrime(int(s1)) or not isPrime(int(s2)):
              isTrunc = False
              break
          s1 = s1[0:-1]
          s2 = s2[1:]
      if isTrunc and next > 10:
          count += 1
          truncPrimes.add(next)
      if count == 11: break
  
  print truncPrimes
  
  print "sum: " + str(sum(truncPrimes))
