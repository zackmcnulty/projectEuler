# logic: start calculating the minimum total path sum to reach a given point. Since you can only move right
# or down, we can see that this implies entry (i,j) will be c_ij + min(c_{i-1j}, c_{ij-1})
# i.e. the min path to entry i, j in the given matrix will be entry_ij + min(entry_{i-1,j}, entry_{i,j-1})

# use dynamic programming concepts to fill in the cummulative path sums, filling in moving from
# left to right then top to bottom.

import time
import numpy as np

start = time.time()

matrix = np.genfromtxt("input_files/p081_matrix.txt", delimiter=",")

# initialize cummulative path sums. We can see that the min path to any entry in first row
# must just be a straight path to the right. Furthermore, the min path to any entry in the
# first column must be a straight path down. 
cum_pathsums = np.zeros((80,80))
cum_pathsums[:,0] = np.cumsum(matrix[:,0])
cum_pathsums[0,:] = np.cumsum(matrix[0,:])

for i in range(1,80):
    for j in range(1,80):
        cum_pathsums[i,j] = matrix[i,j] + min(cum_pathsums[i-1,j], cum_pathsums[i,j-1])

print(cum_pathsums[-1,-1])
print("runtime: ", time.time() - start)
