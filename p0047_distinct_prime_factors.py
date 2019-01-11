  #47: Distinct Prime Factors (correct!)
  from sympy.ntheory import factorint
  
  possNums = list([])
  
  for N in range(1,1000000):
      primeFacts = factorint(N) #gives a dictionary of containing prime factorization key: value = number: multiplicity in factorization
      if len(primeFacts.keys()) == 4: possNums.append(N)
  
  print "factored nums!"
  
  for i in range(0, len(possNums) - 3):
      if possNums[i] + 3 == possNums[i+3]:
          print possNums[i]
  
  print "done!"
