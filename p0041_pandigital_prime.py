 def isPrime(n):
     if n <= 1: return False
     if n == 2: return True
     for div in range(2, int(n**0.5 + 1)):
        if n % div == 0: return False
     return True
 
 
 
 
  
  #41 pandigital primes (correct!)

import itertools as itl    
max = 0
  
  for n in range(1,10):
      nums = itl.permutations([x for x in range(1,n+1)])
  
      for pat in nums:
          s = ""
          for i in pat: s += str(i)
          num = int(s)
          if isPrime(num) and num > max: max = num
  
 print (max)

