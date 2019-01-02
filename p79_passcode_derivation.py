# logic: 



f = open("input_files/p079_keylog.txt")


# key = # and values = list of #s that must be to the right of it based on passcodes

d = {i:[] for i in range(10)}

for line in f:
    d[int(line[0])].append(int(line[1])) 
    d[int(line[0])].append(int(line[2])) 
    d[int(line[1])].append(int(line[2])) 

d2 = {i:set(d[i]) for i in d}
print(d2)


# just looking at the output above, I found 73162890 pretty easily. I was expecting there to be conflicts, or repeated numbers. However,
# there were none...
