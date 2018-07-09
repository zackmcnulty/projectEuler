import time
# correct!

# logic: for each n, find the minimum value of r = r0 such that nCr > 10**6.
# as nCr is symmetric,nCr0 = nCn-r0. Thus all values between r0 and n-r0 satify the condition
# that nCr > 10**6. Also, because of this symmetry, we know we only have to check r values
# up to n/2
# we can move between adjacent nCr values quickly by noticing that
# if r0 + 1 = r1
# nCr0 = n!/r0!(n-r0)!
# then nCr1 = n!/r1!(n-r1)! = n!/(r0 + 1)! (n-r0-1)! -> nCr0*(n-r0)/(r0+1)

# based on the iterative method for calculating nCrm+1 given nCrm (see last line above)
find_nCr1 = lambda r0, nCr0, n: nCr0*(n-r0)/(r0+1)

start = time.time()
count = 0
for n in range(1,101):
    r = 1
    nCr = n
    while r <= n/2:
        if nCr > 10**6:
            count += (n-r) - r + 1
            # this is where I take into account all values of nCr between nCr0 and
            # nCn-r0 will be > 1 mil if nCr0 > 1mil
            break
        nCr = find_nCr1(r, nCr, n)
        r += 1

print count
print time.time() - start
