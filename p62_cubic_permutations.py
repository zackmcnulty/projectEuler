# logic: calculate cubes, and use a dictionary to store the results.
# each key will be a tuple where index i stores a count of the number of digit i in the cube.
# each value will be a set of the cubes with that pattern

def get_digit_counts(n):
    s = str(n)
    counts = [0]*10
    for digit in s:
        counts[int(digit)] += 1

    return tuple(counts)



cube_counts = {(0,1,0,0,0,0,0,0,0,0):[1]}
n = 2
targ_count = 5

while max([len(x) for x in cube_counts.values()] ) < targ_count:
     
    next_digit_counts = get_digit_counts(n**3)
    if not next_digit_counts in cube_counts:
        cube_counts[next_digit_counts] = [n**3] 
    else:
        cube_counts[next_digit_counts].append(n**3)

    n += 1

for key in cube_counts:
    if len(cube_counts[key]) == targ_count: 
        #print(key)
        #print(cube_counts[key])
        print(min(cube_counts[key]))



