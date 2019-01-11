  #2 Even Fib Numbers (CORRECT!)
  
  # I noticed that the even fib numbers are related by En = 4*En-1 + En-2
  
  evens = list([2,8])
  index = 2
  next = 0
  while next < 4*10**6:
      next = 4*evens[index - 1] + evens[index - 2]
      if next < 4*10**6:
          evens.append(next)
          index +=1
  
  print(sum(evens))
