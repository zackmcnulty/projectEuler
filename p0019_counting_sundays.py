  #19: Counting Sundays (correct!)
  # logic: assign a number to each day of week, 0 = sunday, 1 = mon, 2 = tues, etc
  # each month, add the number of days then modulo 7 to figure out what day it is
  day = 1
  
  count = 0;
  for year in range(1900, 2001):
      for month in range(1,13):
          if month in [1, 3, 5, 7, 8, 10, 12]:
              day += 31
          elif month == 2:
              if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
                  day += 29
              else:
                  day += 28
          else:
              day += 30
          if year > 1900 and day % 7 == 0: count += 1
  
  print count
