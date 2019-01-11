  #34 (Correct!)
  def factorial(n):
      if n == 0: return 1
      else: return n*factorial(n-1)
  
  facts = []
  for k in range(0,10): facts.append(factorial(k))

    #facts[i] = i!

  # no 1 digit nums
  # 2 digit nums only include 0-4
  # 3 digit nums only include 0-6
  # 4 digit nums only include 0-7
  # 5 digit nums only include 0-8

  nums = list([])
  for k in range(0, 9999999):
      sum = 0
      n = k
      string = str(k)
      for i in range(0,len(string)):
          sum += facts[int(string[i])]
      if sum == k: print k
  print "done!"
