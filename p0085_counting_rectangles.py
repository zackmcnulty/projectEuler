# logic: Firstly, note that symmetry plays a role in this problem: an n x m
# grid will definitely have the same number of rectangles as an m x n grid
# so WLOG consider only cases where n <= m. 


# For an n x m grid, we can fit (n+1 - k) * (m+1 - l) rectangles of size k x l in it.
# In this case, it is NOT necessarily true that k < l
# Thus, the total number of rectangles is
# sum_k^n (sum_l^m ((n+1 - k) * (m+1 - l))
# = sum_k^n ((n+1 - k) sum_l^m (m+1 - l))
# = sum_k^n ((n+1 - k)*(m(m+1) - sum_l^m ( l))
# = sum_k^n ((n+1 - k)*(m(m+1) - m(m+1)/2)
# = sum_k^n ((n+1 - k)*(m(m+1)/2)
# = m(m+1)/2 (n(n+1)/2)
# 1/4 (nm(n+1)(m+1)

# so we are interested in finding 1/4nm(n+1)(m+1) as close to 2 million as possible, with n <= m

# since we can see that the number of rectanges is of order n^2m^2, we can assume that nm < 2*10**3
# once we generate possible pairs, simply find the one that generates a value closet to 2 million!

max_val = 2*10**2
poss_vals = [(x,y) for x in range(1,max_val) for y in range(x, max_val)]

min_val = 10**5
best_pair = (0,0)
fn = lambda x,y: abs(8*10**6 - x*y*(x+1)*(y+1))

for val in poss_vals:
    next_fn = fn(val[0], val[1])
    if next_fn < min_val:
        min_val = next_fn
        best_pair = val

print (best_pair)


# a shorter but less clear version. However
from functools import reduce
print(reduce(lambda x,y: (x if fn(x[0], x[1]) < fn(y[0], y[1]) else y), poss_vals))



