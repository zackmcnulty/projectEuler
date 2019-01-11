  # 36: double base palindromes (correct!)
  def isPal(s):
      n = len(s)
      left = s[:(n+1)/2]
      right = s[n/2:]
      return left == right[::-1]
  
  coolPals = set([])
  
  for num in range(1,10**6):
      binary = str(bin(num))[2:]
      if isPal(str(num)) and isPal(binary): coolPals.add(num)
  
  print sum(coolPals)
