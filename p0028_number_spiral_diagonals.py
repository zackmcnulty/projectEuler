  #28 Number Spiral Diagonals (correct)
  
  def numGenerator(maxDim):
      cur = 1
      n = 3
      while n <= maxDim:
          for i in range(0,4): # 4 corners of box
              cur += n - 1
              yield cur
          n += 2
  
  print 1+sum(numGenerator(1001))
