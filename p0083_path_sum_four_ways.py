# logic: pretty much just uses Dijstrkas algorithm to find the min path


import time
import numpy as np

start = time.time()

matrix = np.genfromtxt("input_files/p083_matrix.txt", delimiter=",")
cumpathsum = np.ones((80,80)) * 10**6

# whether we have chosen a given entry; i.e. this entry is a min
not_used = np.ones((80,80), dtype=bool)


cumpathsum[0,0] = matrix[0,0]
while cumpathsum[-1,-1] == 10**6:
    # this will be the index of the array, which can be used to

    min_val = cumpathsum[not_used][ np.argmin(cumpathsum[not_used])]
    idx = np.where(cumpathsum == min_val)

    i = -1
    k = 0

    # sometimes, the min value occurs twice, and its possible one of these min vals
    # occurs at a previously chosen index. This helps ignore previously chosen indices.
    while i < 0 or not_used[i,j] == 0:
        i = idx[0][k]
        j = idx[1][k]
        k+=1
        
    not_used[i,j] = False 

    if i != 0:
        cumpathsum[i-1,j] = min(cumpathsum[i-1,j], matrix[i-1,j] + cumpathsum[i,j])
    if j != 0:
        cumpathsum[i,j-1] = min(cumpathsum[i,j-1], matrix[i,j-1] + cumpathsum[i,j])
    if i != 79:
        cumpathsum[i+1,j] = min(cumpathsum[i+1,j], matrix[i+1,j] + cumpathsum[i,j])
    if j != 79:
        cumpathsum[i,j+1] = min(cumpathsum[i,j+1], matrix[i,j+1] + cumpathsum[i,j])
#    time.sleep(1)

print(cumpathsum[-1,-1])
print("runtime: ", time.time() - start)
