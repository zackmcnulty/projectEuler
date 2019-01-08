#logic: keep track of all the numbers that end in 1 or 89. If we ever reach one of these during our transformations
# we know where the current number must end!

import time
ends89 = set([])
ends1 = set([])

for num in range(1, 10**7):
    print(num)
    n = num
    while n != 1 and n != 89:
        temp = 0
        for digit in str(n):
            temp += int(digit)**2
        n = temp

        if n in ends89: 
            ends89.add(num)
            break
        if n in ends1:
            ends1.add(num)
            break
    else:
        if n == 1: ends1.add(num)
        else: ends89.add(num)

print(len(ends89))
