# 33 Digit Cancelling fractions (correct!)
      # logic: for the digits to "cancel" numerator and denominator must have a common digit.
      # Ignore 0 as a possible common digit (leads to trivial case)
      # for digits 1-9, check all possibilities with number in first position
      # i.e. 1x/1y, then 1x/y1, then x1/1y then x1/y1 (last case not possible?)
  prod = 1
  
  for i in range(1,10):
      for x in range(1,10):
          for y in range(1,10):
              num1 = (10.0*i + x)/(10.0*i + y)
              num2 = (10.0 * x + i) / (10.0* i + y)
              num3 = (10.0*x + i)/(10.0*y + i)
              num4 = (10*i + x)/(10.0*y + i)
              for num in [num1, num2, num3, num4]:
                  if num == 1.0*x/y and num < 1:
                     prod*= num
  
  print prod

