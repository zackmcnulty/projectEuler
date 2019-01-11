  #32 pandigital products (Correct!)
  
  def isPandNum(s):
      if not len(s) == 9:
          return False
  
      allNums = set([str(x) for x in range(1, 10)])
      sNums = set(s)
      missingNums = allNums.difference(sNums)
      if len(missingNums) == 0:
          return True
  
      else:
          return False
  
  
  
  pandNums = set([])
  
  for i in range(1,1000):
      for j in range(1,10000):
          if isPandNum(str(i) + str(j) + str(i*j)): pandNums.add(i*j)
  
  print (pandNums)
  print sum(pandNums)
