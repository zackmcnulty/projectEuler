  # 31 Coin Sums (correct!)
      # we will use recursive backtracking to find every working combination
  
  def findCoinSum(left, coinValues, index):
      if index == 7: return 1
      denom = coinValues[index]
      sum = 0
      for i in range(0, left/denom + 1):
          sum += findCoinSum(left - i*denom, coinValues, index + 1)
      return sum
  
  
  coinValues = list([200,100,50,20,10,5,2,1])
  print findCoinSum(200, coinValues, 0)
