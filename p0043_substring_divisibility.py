  #43 : substring divisibilty (correct!)
  
import itertools as itl

  def coolSubs(s):
      start = 2
      end = 4
      divs = [2,3,5,7,11,13,17]
      for i in range(0,7):
          if int(s[start + i - 1: end + i]) % divs[i] != 0: return False
      return True
  
  coolNums = set([])
  
  nums = itl.permutations([x for x in range(0,10)])
  
  for pat in nums:
      s = ""
      for i in pat: s += str(i)
      if coolSubs(s) and s[0] != "0":  coolNums.add(int(s))
  
  print (coolNums)
  print (sum(coolNums))
