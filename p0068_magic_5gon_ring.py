# logic: rather than creating the actual graph, we can simply label the graph
# vertices with the indices 0 to 9. Then, to test a possible labeling of the graph
# we can simply just work with the permutations of 1-10 in a list.

# starting at top left vertice, label this 0 and going clockwise label the outer vertices 1,2,3,4 (i.e. 0, ..., n-1). Then,
# starting at the vertex connected to vertex 0 in the inner ring, label these vertices 5,6,7,8,9 (i.e. n, ..., 2n-1) going clockwise.

# inefficiencies: many permutations generate isomorphic graphs (i.e. labeling differs only by rotations)
# ideally, we instead only loop over each labeling once: how?


import itertools as itl
import time

n = 5 # allows for expanding to different sized n-gons. i.e. n = 5 is a 5-gon
desired_length = 16 # what sequence length is desired

# l = current graph labeling, as a list, in order described above.
# checks if labeling is valid (i.e. all row sums are equal)
def check_valid_labeling(l):
    rowsum = l[0] + l[n] + l[n+1]
    for i in range(1, n):
        if l[i] + l[n+i] + l[n + ( (i + 1) % n)] != rowsum: return False

    return True


def get_seq(l):
    m = min(l[:n])
    idx = l.index(m)
    seq = ""

    for i in range(0,n):
        seq += str( l[(idx+i) % n] )
        seq += str( l[n + ( (idx + i) % n)] )
        seq += str( l[n + ( (idx + i + 1) % n)] )

    return seq


possible_labelings = itl.permutations(list(range(1,2*n+1)))

valid_labelings = set([])

for labeling in possible_labelings:
    if check_valid_labeling(labeling):
        vl = get_seq(labeling)
        if len(vl) == desired_length:
            valid_labelings.add(int(vl)) 


print(max(valid_labelings))


