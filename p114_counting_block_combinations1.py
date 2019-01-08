# logic: use dynamic programming instead of recursion
# Consider the task of constructing a valid coloring of this row of blocks. Starting at the far left,
# we consider what might occur in a valid coloring. 
# 1) it could start with a black block, followed by a valid row of n-1 blocks
# 2) it could start with a streak of k >= 3 red blocks then a black block., follwed by a valid row of n-k-1 blocks
# 3) it could start with a streak of n red blocks (i.e. whole row is red)

# Naturally, this problem seems to lend itself to recursion/dynamic programming 

max_n = 50

#  num_ways[i] = number of valid colorings of a row of size i 
num_ways = [0] * (max_n + 1)

# if we have less than 3 blocks in our row, the only valid coloring will be all black blocks
num_ways[0:3] = [1]*3 

for n in range(3, max_n + 1):
    #           = first block black + next block of size i is red, followed by a black block + all remaining blocks red (in one way)
    num_ways[n] = num_ways[n-1] + sum([num_ways[n-i-1] for i in range(3, n)]) + 1

print(num_ways[50])
