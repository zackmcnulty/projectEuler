  #5 smallest multiple (correct!)
  
  # numbers that matter 20, 19, 18, 17, 16,15,14,13,12,11, (others are factors of these anyways)
  # 10 9 8 7 6
  current = 20
  notDone = True
  while notDone:
      for k in range(11,20):
          if not current % k == 0:
              current += 20
              break
          elif k == 19: notDone = False
  
  print (current)

