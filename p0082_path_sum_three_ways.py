# logic: calculate the min path sums to any given entry a column at a time. Again, we see that the min
# path sum to entry ij can be represented by: entry_ij + min(pathsum_{i-1j}, pathsum{ij-1}, pathsum{ij+1})


import time
import numpy as np

start = time.time()

matrix = np.genfromtxt("input_files/p082_matrix.txt", delimiter=",")
cumpathsum = np.zeros((80,80))


# initializing cummulative path sums. Clearly, as all entries are positive. The first column
# will be the same as the matrix itself (we wouldnt take a path from one element in first column
# to another element in first column.
cumpathsum[:,0] = matrix[:,0]

# we calculate the min path sums from top down, then left to right. So we always know the higher entries first.
# Thus, when calculating a new min path sum, we can either come from above (with path sum cumpathsum[i-1,j] + matrix[i,j])
# or we can come from below. If we come from below, we can consider moving from the column to the left and then moving upward.
# the new path sum is then the cumpathsum from whichever entry in the previous column we start with plus the path sum moving up
# which is calculated using np.cumsum(matrix[i:,j])
for j in range(1,79):
    for i in range(80):
        if i == 0:
            cumpathsum[i,j] = min(np.add(np.cumsum(matrix[i:, j]) , cumpathsum[i:, j-1]))
        else:
            cumpathsum[i,j] = min(np.append(cumpathsum[i-1,j] + matrix[i,j] , np.add(np.cumsum(matrix[i:, j]) , cumpathsum[i:, j-1])))
    print(cumpathsum)
cumpathsum[:, -1] = matrix[:, -1] + cumpathsum[:,-2]

print(cumpathsum)

print(min(cumpathsum[:,-1]))
print("runtime: ", time.time() - start)
