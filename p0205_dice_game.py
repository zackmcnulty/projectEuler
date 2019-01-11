# 205 Dice Game (CORRECT!!!!!!!!!!)
  # Logic: first I will generate lists of all possible sums, with duplicates, and then sort them f>
  # next I will traverse the two lists simultaneously, starting at index 0 for pete. I will move d>
  # list as long as Pete's sum is greater, and add this to the counts of outcomes where pete "wins"
  # when I reach a point where pete's sum is less, step forward, and start the number of winning c>
  # this next peteSum at the max of the previous (since the list is ascending, we know this sum is>
  # than all the sums of colins that the previous pete sum was).
  
  
  peteSums = list([])
  colinSums = list([])
  
  def rollDice(left, max, curSum, sums):
      if left == 0: sums.append(curSum)
      else:
          for roll in range(1,max + 1):
              rollDice(left - 1, max, curSum + roll, sums)
  
  rollDice(9, 4, 0, peteSums)
  rollDice(6,6, 0, colinSums)
  
  peteSums.sort()
  colinSums.sort()
  
  totalPete = len(peteSums)
  totalColin = len(colinSums)
  
  
  possibleOutcomes = totalColin * totalPete
  
  peteI = 0
  colI = 0
  outcomesPeteWins = 0  # number of outcomes where pete wins
  curCount = 0 # number of outcomes pete wins for this current index
  

    # We now have two ascending lists representing all the possible sums. For each of Pete's possible
  # outcomes, we need to find the number of colin's outcomes it beats! To do so, we do a dual list traversal
  # I start at beginning of both lists. If pete > col, pete wins that outcome! Add that to the curCount of wins.
  # and look at next num in colin's list. Continue until pete reaches a point where he loses (or draws).
  # then move pete forward. As the next number in petes list is >= the last one, we know it would have won
  # in all the outcomes where the last one won, so instead of reseting current count and starting at beginning
  # of collin's list, we can just let this new number start with the same number of wins as the previous, and
  # move forward from there!
  while peteI < totalPete and colI < totalColin:
      if peteSums[peteI] > colinSums[colI]:
          curCount += 1
          colI += 1
      else:
          outcomesPeteWins += curCount
          peteI += 1

  # fence posting
  if not peteI == len(peteSums) - 1: #reached end of colin's list first
      for ind in range(peteI, totalPete): outcomesPeteWins += curCount
      #if we stopped before reaching end of pete's list, all elements from the current one in Pete's
      # list are greater than the entirety of Colins list. Thus add all of colins list


  #now we have the number of outcomes where Pete wins! Divide by total number of possible outcomes
  print (1.0*outcomesPeteWins)/possibleOutcomes
