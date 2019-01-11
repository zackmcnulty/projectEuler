  #624 Two Heads are better than 1 (NOT DONE)
_ 
  from decimal import *
  from fractions import Fraction
  
  #using Binet's formula, we can derive the sum of all these probabilities, and reduce it
  # using the formula for a geometric series. We know P(n) = sum (n-1)th prime/2^n based on
  # playing with some of the probabilities
  
  def PofN(n):
      val = 1/math.sqrt(5) * (  (2/(1+math.sqrt(5))  *  ((1 + math.sqrt(5)) /4)**n) * (1 / (1 - ((>
      return Fraction(val).limit_denominator(1000000000000000000000000)
  #IT FUCKING WORKED! (can handle smaller values. Now just need to find a way to relate them to la>
  # so I can calculate P(10**18)
  pvals = [PofN(n) for n in range(1,20)]
  
  plt.plot(pvals)
  plt.plot(pvals, 'ro')
  plt.show()
  
  print "done!"
  
  time.sleep(100)
  
  
  
  nthFib = lambda n:int((((1+ math.sqrt(5))**(n-1))-((1 - math.sqrt(5))**(n-1)))/((2**(n-1))* math>
  # returns fib of (n+1) position
  
  calcProb = lambda mult, maxN: sum([Decimal(nthFib(mult*i))/Decimal((2**(i*mult))) for i in range>
  
  for n in range(1,10): print nthFib(n)
  
  pCount = calcProb(2,100)
  P = Fraction(pCount).limit_denominator(1000000000)
  print pCount
  #P5 = 97/671
  #P10 = 633/16775



    # yeilds the probability we stop flipping (i.e. we get two heads) at flip numbers that are
  # multiples of mult, up to a max number of flips maxN
  def flipProbs(maxN, mult):
      # dont need : yield 0
      cur = 1
      last = 0
      fibCount = 2
      while fibCount < maxN:
          if fibCount % mult == 0:
              yield Decimal(cur)/Decimal(2**fibCount)
          temp = cur
          cur = cur + last
          last = temp
          fibCount += 1

  sum = 0
  for prob in flipProbs(10**36,10**18): # very accurate....
      sum += prob

  print sum



  def findEndSeq(n, counts, curLevel):
      findHelp(n, counts, 1, True)
      findHelp(n, counts, 1, False)

  def findHelp(n, counts, curLevel, lastIsHeads):
      if curLevel < n:
          if lastIsHeads:
              counts[curLevel] += 1
              findHelp(n, counts, curLevel + 1, False)
          else:
              findHelp(n, counts, curLevel + 1, True)
              findHelp(n, counts, curLevel + 1, False)

  n = 20
  counts = list([0 for i in range(0,n)])
  findEndSeq(n, counts, 0)

  print counts
  # forms the fibonnaci sequence? dividing by the number of possible outcomes at each
  # number of coin flips (1 + index of entry in counts; outcomes = 2^ # flips)
  # we see this sequence is actually 1/2 of a very common sequence. Something about
  # Binet's formula can be used to calculate a value of sequence?
  # can skip the simuation know and just know that the probability of it ending at
  # flip n is the (nth fib number)/2^n

