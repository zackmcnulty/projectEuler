# logic: starting at the lower numbers, store the length of their chains in
#        a hash map for fast accessing. If a larger number is determined to 
#        form that chain, add it so we can skip it later. Rather than following
#        every chain to completion, we can check if a number is already in this set

import time 
factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def factorial_sum(n):
    total = 0
    for digit in str(n):
        total += factorials[int(digit)]
    return total

#print(factorial_sum(2))
#time.sleep(100)
known_cycles = {}

for n in range(1, 20):
    #print(n)
    all_nums = {n:0}
    ind = 1
    num = n
    while True:
        num = factorial_sum(num)
        if num in all_nums:
            length = ind - all_nums[num]
            known_cycles[n] = length
            known_cycles[num] = length
            break
        elif num in known_cycles:
            known_cycles[n] = known_cycles[num]
            break
        else:
            all_nums[num] = ind
            ind += 1
    
    print("n: ", n, ", all_nums: ", all_nums)
    print('known_cycles[n] = ', known_cycles[n])
    print(known_cycles)

        
count = 0
for num in known_cycles:
    if known_cycles[num] == 60 and num < 10**6: count += 1

print(count)
print(known_cycles[69])
