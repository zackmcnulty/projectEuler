# logic: convert everything to the same base, then just compare the exponents. Arbitrarily, I will
# convert everything to base two. For example,
# a^b = 10^x --> log a^b = x --> x = b log a
# i.e. if a^b > x^y then b log a > y log x

import math
import time

start = time.time()

f = open("input_files/p099_base_exp.txt")
max_line_num = 0
max_val = 0

for line_num, line in enumerate(f):
    base_exp = line.split(",")
    next_val = int(base_exp[1]) * math.log10(int(base_exp[0]))
    if next_val > max_val:
        max_val = next_val
        max_line_num = line_num

# +1 accounts for the fact that lines are numbered starting at 0
print(max_line_num + 1)
print("runtime: ", time.time() - start) 
