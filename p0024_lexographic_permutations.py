  # 24 Lexicographic Permutations (correct!)
          # figure out how many ways to
  
  def factorial(n):
      if n == 1: return 1
      else: return n*factorial(n-1)
  
  numsLeft = list([0,1,2,3,4,5,6,7,8,9])
  curPos = 0
  pattern = ""
  
  while not len(numsLeft) == 1:
      n = len(numsLeft)
      index = 0
      perms = factorial(n-1)
      # If we have n items left, there are (n-1)! permutations that have a specific next digit
      # the first perms permutations have the lowest digit remaining at the front,
      # then the next perm permutations have the next lowest digit. So keep moving forward until the
      # position count exceeds 1 million. Then we know we cannot move to the next digit without passing
      # over the combination we want. So we move on to the next digit and repeat.
      while curPos < 10**6:
          curPos += perms
          index += 1
      curPos -= perms
      index -= 1
      pattern += str(numsLeft[index])
      del numsLeft[index]
  
  print pattern + str(numsLeft[0])
