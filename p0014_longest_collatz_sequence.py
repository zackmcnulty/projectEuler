  # 14 Longest Collatz Sequence (correct!)
  def ColSeq(n): 
      if n == 1:
          return 1
      elif n % 2 == 0:
          return 1 + ColSeq(n/2)
      else:
          return 1 + ColSeq(3*n + 1)
  
  maxLength = 0
  bestNum = 0
  for n in range(1, 10**6):
      nextLength = ColSeq(n)
      if nextLength > maxLength:
          maxLength = nextLength
          bestNum = n
  
  
  print bestNum
  

