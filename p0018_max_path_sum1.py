  #18: max path sum (CORRECT!)
  #start at second to last row; Set each entry to be its value + max of values below it;
  # move up one row and repeat process.
  rowBelow = list([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])
  while True:
      nextRow = list(input("Next Row?: "))
      for i, val in enumerate(nextRow): # i = index, val = current val in that index
          nextRow[i] = val + max(rowBelow[i], rowBelow[i + 1])
      print nextRow
      rowBelow = nextRow
