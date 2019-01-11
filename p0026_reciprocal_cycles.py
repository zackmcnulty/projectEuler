  # 26 Reciprocal Cycles (CORRECT!)
  #logic: convert all these decimals into strings, and separate them at the "." decimal point. If >
  # right side starts with the left side, we have a repeating sequence. If not, move the
  # decimal place forward 1 spot by multiplying by 10 and check again
  
  
  from decimal import *
  decis = 2000
  getcontext().prec = decis
          
  maxD = 7
  maxPattern = 6
          
  
  for d in range(10,1000):
      num = Decimal(1) / Decimal(d)
      while num < 0.1: num = num * 10
      for patLength in range(1, decis/2):
          numStr = str(num*10**patLength)
          parts = numStr.split(".")
          if len(parts) > 1 and parts[1].startswith(parts[0]):
              if patLength > maxPattern:
                  maxPattern = patLength
                  maxD = d
              break
  
  print maxD
  print maxPattern
