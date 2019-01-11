  # 39 Champernownes Constant (correct!)
  
  #logic; for 1 digit numbers, there are 9 such numbers (thus 9 digits), for 2 d>
  # there are 9*10 such numbers ( and thus 2*9*10 such digits),
  # for 3 digit numbers, there are 9*10*10 (and thus 3*9*10*10 such digits)...
  # use this pattern to figure out where the number lies.
  # first step, I try to figure out how many digits the number has.
  # Then once I know that, I have reduced my n value such that it represents the>
  # the digit of interest when considering only numbers with the determined numb>
  # So if it was found there are 4 digits, and n = 121, since each number has 4 >
  # at the 31st number. From there, I can subtract 30*4 and see I want the first>
  
  
  def dn(n):
      digits = 1
      while n > 0:
          subtract = digits*9*(10**(digits - 1))
          n -= subtract
          digits += 1
      digits -= 1
      n += subtract
  
      numOfInterest = 10**(digits-1) + (n-1)/digits
      return str(numOfInterest)[n%digits - 1]
  
  nVals = [10**x for x in range(0, 7)]
  
  prod = 1
  for n in nVals:
      prod *= int(dn(n))
  
  print( prod)
  

