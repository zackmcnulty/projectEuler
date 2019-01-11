  # 30: Digit Fifth Powers (correct!)
  
  totalSum = 0
  for num in range(2,10**6):
      digits = str(num)
      sum = 0
      for next in digits:
          sum += int(next)**5
      if sum == num: totalSum += num
  
  print totalSum
