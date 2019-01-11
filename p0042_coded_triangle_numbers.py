  # 42: Coded Triangle Numbers (correct!)
  relevantTris = []
  
  tri = lambda n: (n+1)*n/2
  for n in range(1,50): relevantTris.append(tri(n))
  
  print (relevantTris)
  
  with(open('p042_words.txt')) as inputFile:
      count = 0
      for line in inputFile:
          list = line.strip().replace("\"", "")
          words = list.split(",")
  
      for w in words:
          letterSum = 0
          for letter in w:
              letterSum += ord(letter) - 64
          if letterSum in relevantTris: count += 1
  
  print (count)

