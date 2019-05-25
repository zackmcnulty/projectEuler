# logic: The numerator and denominator are only irreducible if the two are relatively prime (i.e. GCD == 1).
# Furthermore, why bother looking for all fractions when we only care about those in range 1/3 to 1/2. 
# For each denominator, this vastly restricts the possible numerators we have to look at.

# we wont have to worry about reducing the fractions because if there is a way to reduce the fraction to a smaller
# dominator, we would have found it in previous iterations

def gcd(a,b):
    while b != 0 :
        t = b
        b = a % b
        a = t
    return a

count = 0
for d in range(1, 12001):
    #print(d)
    for n in range( d // 3 + 1, (d+1)//2):
        if gcd(d,n) == 1:
            count += 1


print(count)
