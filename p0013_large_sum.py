  # 13: large sum (Correct)
  with(open('50digitnums.txt')) as inputFile:
      sum = 0
      for line in inputFile:
          sum += int(line)
      s = str(sum)
      print (s[0:10])
