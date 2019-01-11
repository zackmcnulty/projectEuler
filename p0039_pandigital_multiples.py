def isPandNum(s):
    if not len(s) == 9:
         return False

     allNums = set([str(x) for x in range(1, 10)])
     sNums = set(s)
     missingNums = allNums.difference(sNums)
     if len(missingNums) == 0:
         return True

     else:
         return False

 # 38 pandigital multiples (correct!)
 # as n > 1, we have at least two numbers being concatinated. This means each n>
 # ( we have 9 digits total, so its possible x * 1 = 4 digits and x*2 = 5 digit>
 # x is at most 4 digits.
max = 0
 
for x in range(1, 10000):
    s = ""
    n = 1
    while len(s) < 9:
        s += str(x*n)
        n += 1
    if isPandNum(s) and int(s) > max: max = int(s)
  
print (max)
