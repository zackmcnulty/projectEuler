# logic: 
#  - since the square ends in 0, we know our positive integer ends in 0
#  - between sqrt(102030405060708090) =  1010101010.1 and sqrt(192939495969798990) = 1389026623.311

import time


start = time.time()


for n in range(1010101010, 1389026630,10):
    s = str(n**2)
    if s[::2] == "1234567890":
        print(n)
        break


print("runtime: ", time.time() - start)
