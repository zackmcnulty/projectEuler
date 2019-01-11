  #67: max path sum (CORRECT!)
  # same logic as #18 below, but automated to run of txt file of nums
  #start at second to last row; Set each entry to be its value + max of values below it;
  # move up one row and repeat process.
  results = []
  with(open('p067_triangle.txt')) as inputFile:
      for line in inputFile:
          line = line.strip()
          results.append(list(line.split(" ")))
  lastRow = results[-1]
  curRow = -2
  aboveRow = results[curRow]
  while len(aboveRow) > 1:
      for i, val in enumerate(aboveRow):
          aboveRow[i] = int(val) + max(int(lastRow[i]), int(lastRow[i + 1]))
      lastRow = aboveRow
      curRow -= 1
      aboveRow = results[curRow]

  maxPath = int(results[0][0]) + max(int(lastRow[0]), int(lastRow[1]))
  print (maxPath)
