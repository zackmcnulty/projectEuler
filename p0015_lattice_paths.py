  # 15 Lattice Paths (correct!)
  
  #solved without code: try thinking of the fact that you have 40 moves to make, 20 rights and 20 downs.
  # so you have 40 slots to fill, 20 with rights and the rest with downs. There are 40 choose 20 ways to fill
  # those first 20 slots, and the rest are just filled with downs.
  
  def countPaths(N):
      downsLeft = N
      rightsLeft = N
      print countHelp(downsLeft, rightsLeft)
  
  def countHelp(downs, rights):
      if downs == 0 or rights == 0: return 1
      else:
          return countHelp(downs - 1, rights) + countHelp(downs, rights - 1)
  
  for n in range(1,21):
      countPaths(n)
