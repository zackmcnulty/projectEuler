  def isPrime(n):
+     if n <= 1: return False
+     if n == 2: return True
      for div in range(2, int(n**0.5 + 1)):
          if n % div == 0: return False
      return True
_ 
_ 
  #7 10001st prime (correct!):
  def isPrime(n):
      for facts in range(2, int(n**0.5) + 1):
          if n % facts == 0: return False
      return True
  
  count = 1
  num = 1
  while count < 10001:
      num += 2
      if isPrime(num):
          count += 1
  print num
