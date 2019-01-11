  #10: Sum of Primes (correct!)
  # logic: brute force; check all possible numbers as factors up to sqrt(n)
  
  def isPrime(n):
      for facts in range(2, int(n**0.5) + 1):
          if n % facts == 0: return False
      return True
  
  sum = 0
  for n in range(2, 2*(10**6)):
      if isPrime(n):
          sum += n
  
  
  print sum

