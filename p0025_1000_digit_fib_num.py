  # 25: 1000-digit fibonacci number (correct!)
  
  def fib():
      last = 0
      cur = 1
      while True:
          yield cur
          temp = last
          last = cur
          cur = temp + cur
  
  for n, fib in enumerate(fib()):
      if len(str(fib)) >= 1000:
          print "index: " + str(n + 1)
          break

