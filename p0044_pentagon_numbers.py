  # 44: Pentagon numbers
  
  #logic: given the formula for a pentagon number, we can check if any number is>
  # by solving for n. If n is a natural number, the number is pentagon. Else it >
  # This will allow us to quickly check if numbers are pentagon
  start = time.time()
  
  pNums = set(n*(3*n-1)/2 for n in range(1, 2400))
  #def isPent(pn):
      #n = math.sqrt((2.0/3.0)*pn + 1.0/36.0) + 1.0/6.0
      #return abs(n - round(n)) < 0.001
  
  possible = set([])
  
  for j,k in itl.combinations(pNums, 2):
      if j+k in pNums and abs(j-k) in pNums:
          possible.add(abs(j-k))
  
  print min(possible)
  
  
  end = time.time()
  print end - start
