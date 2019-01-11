# Problem 39: Integer right triangles (CORRECT)
  
  # a + b + c <= 1000
  # a = st, b = (s^2 - t^2)/2, c = (s^2 + t^2)/2
  # all triples: m(2k+1)(k+n+1) <= 500 for k>n>=0 and m > 0
  
  
  def getP(m, k, n):
      return m*(2*k + 1)*2*(k+n+1)
  
  myRims = dict([])
  
  m = 1
  k = 1
  n = 0
  while (2*k + 1)*(k+1) <= 500:
      for n in range(0, k):
          nextP = getP(m,k,n)
          if nextP > 1000: break
          elif myRims.has_key(nextP):
              myRims[nextP] += 1
          else:
              myRims[nextP] = 1
      k += 1
  
  newTerms = dict([])
  for keys in myRims:
      m = 2
      while m*keys <= 1000:
          if newTerms.has_key(m*keys):
              newTerms[m*keys] +=1
          else:
              newTerms[m*keys] = 1
          m += 1
  
  for key in newTerms:
      if myRims.has_key(key): myRims[key] += newTerms[key]
      else: myRims[key] = newTerms[key]
  
  max = 0
  bestKey = 0

  for key in myRims:
      if myRims[key] > max:
          max = myRims[key]
          bestKey = key

  print(str(bestKey) + ", " + str(max))
