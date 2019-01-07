# logic: It seems like simply providing the minimum spanning tree of the network, which we can easily do
# using kruskals algorithm

import time
import numpy as np

class DisjointSet:


    def __init__(self):
        # dictionary that converts array indices to desired object
        self.converter = {}
        
        # displays hierarchy
        self.pointers = []
        self.size = 0
        self.parts = 0

    def make_set(self,n):
        self.converter[n] = self.size
        self.pointers.append(-1)
        self.size += 1
        self.parts += 1

    def find_set_helper(self, index):
        if (self.pointers[index] < 0):
            return index
        else:
            top_index = self.find_set_helper(self.pointers[index])
            self.pointers[index] = top_index
            return top_index


    def find_set(self,n):
        return self.find_set_helper(self.converter[n])

    # union by size
    def union(self, a , b):
        head1 = self.find_set(a)
        head2 = self.find_set(b)
        if head1 == head2:
            raise ValueError("The given two elements are already in the same set")

        # in this case, since the sizes are stored with negative numbers, a smaller number
        # represents a larger set
        elif self.pointers[head1] < self.pointers[head2]:
            self.pointers[head1] += self.pointers[head2]
            self.pointers[head2] = head1
        else:
            self.pointers[head2] += self.pointers[head1]
            self.pointers[head1] = head2
        
        self.parts -= 1

    def get_parts(self):
        return self.parts





start = time.time()

f = open("input_files/p107_network.txt").read()

# set high value to represent non-edge
f = f.replace("-", "100000000")
f2 = open("input_files/p107_network2.txt", "w")
f2.write(f)
f2.close()


network = np.loadtxt("input_files/p107_network2.txt", delimiter=",")

# divide by two because each edge is counted twice. i.e. entry i,j and j,i both count the same
# edge
start_weight = np.sum(network[network != 100000000]) / 2 
print("start total weight: ", start_weight)

ds = DisjointSet()
for i in range(0,40):
    ds.make_set(i)


new_weight = 0

while ds.get_parts() != 1:
    # find the minimum element in our network remaining.

    ind = np.unravel_index(np.argmin(network, axis=None), network.shape)
    
    # try to union the sets; if it fails, the two vertices are already connected via some
    # path so no need to add this edge. If it doesn't add this edge and count its weight.
    # Either way, set new edge weight to 10000000 so it isnt chosen again
    try: 
        ds.union(ind[0], ind[1])        
        new_weight += network[ind]
    except ValueError:
        x = 1   
        # do nothing 

    network[ind[0], ind[1]] = 10000000
    network[ind[0], ind[1]] = 10000000


print ("weight change: ", start_weight - new_weight)
print("runtime: ", time.time() - start)


