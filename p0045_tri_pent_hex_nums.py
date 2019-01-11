  #45: pentagonal, trigonal, and hexagonal numbers
  # Logic:Since the hexagonal numbers increase faster, if we loop through every >
  # check if it is tri/pent, we have less numbers to check. Solving Pn, Tn for n>
  # find formulas to see if a number is pentagonal or triagonal (the n given sho>
  start = time.time()
  
  def hexNum():
      n = 1
      while True:
          yield n*(2*n - 1)
          n += 1
  
  def isPent(n):
      return ((math.sqrt(24*n + 1) + 1) % 6) == 0
  
  def isTri(n):
      return ((math.sqrt(8*n + 1) - 1) % 2) == 0
  
  for next in hexNum():
      if isPent(next) and isTri(next) and next > 40755:
          print(next)
          break
  
  end = time.time()
  print end - start
