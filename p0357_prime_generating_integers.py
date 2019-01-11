  # 357 Prime Generating integers
      # n cannot be divisible by 4 (then it would be divisible by 2 but 2 + n/2 would be even)
      # n cannot be odd: n cannot be product of odd numbers;
          #if ab = n for odd a,b, then a + n/a= a + b = sum of two odds = even (not prime)
      # n cannot be square: if n = a^2 then a + n/a = a + a = 2a is even and thus not prime
      # n cannot be 2*square?????
      #n cannot be the product of two even numbers (same as cannot be divisible by 4)
  
      # i.e. n is the product of 1 even number x and 1 odd number y such that x + n/x is prime and y + n/y
          # i.e. x + y is prime
          # note: as 1, n are factors of n this implies that n + 1 is prime. i.e. n is one less than a prime
              # most numbers 1 less than prime satisfy this (besides 18,66 because 6 + 3 = 9)
              #satisfy this property
  
          # every even number > 2 can be written as sum of two primes
              #p1 + p2 = e :  so d + n/d = d + (p1 + p2)/d. Choose d = p2: p2 + 1 + p1/p2????
  
          # search through all possible values of x and y such that xy < 100000000. If I find a none prime, cross it off the list!
