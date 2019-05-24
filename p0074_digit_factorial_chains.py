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

for n in range(1, 10**6):
    #print(n)
    if n not in known_cycles:
        all_nums = {n:0}
        ind = 1
        num = n
        while True:
            num = factorial_sum(num)
#            if num in known_cycles:
                # If I see a number that I know cycles, then in (cycle length - 1) turns I will see that number again!
                # Dont forget to add ind, the number of numbers I have already seen
#                known_cycles[n] = ind + known_cycles[num]
#                break
            if num in all_nums:
                # If I see the same number twice, I am done. Not only do I know the cycle length of the current n, but
                # the cycle length of num!
                length = ind - all_nums[num]
                known_cycles[n] = ind
                known_cycles[num] = length
                break

            all_nums[num] = ind
            ind += 1
        
        #print("n: ", n, ", all_nums: ", all_nums)
        #print(n)
        #print('known_cycles[n] = ', known_cycles[n])
        #print(known_cycles)

        
count = 0
for num in known_cycles:
    if known_cycles[num] == 60 and num < 10**6: count += 1

print(count)
print(known_cycles[78])
print(known_cycles[540])
print(known_cycles[169])
