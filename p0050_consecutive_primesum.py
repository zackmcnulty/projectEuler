  # 50 Consecutive Prime Sum (correct!)
  #logic: must include an odd number of terms, otherwise it cannot be a prime
  
  primes = filter(lambda x: isPrime(x), [x for x in range(2,10**6)])
  
  terms = list([(2*x + 1) for x in range(260,300)])
  
  for nextTerm in terms:
      print "terms: " + str(nextTerm)
      for i in range(0, 10**2):
          primeSum = sum(primes[i:i+nextTerm])
          if primeSum in primes:
              print str(primeSum)
  
  print "done!"
