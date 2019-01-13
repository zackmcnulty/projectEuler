# logic: First, note that sum_{i=1} i^2 = n(n+1)(2n+1)/6
# Therefore, we can represent any consecutive sum by n(n+1)(2n+1)/6 - m(m+1)(2m+1)/6
# Since we must have at least  two numbers to make up a sum keep this in mind.
# Also, n^2 < 10^8 --> , n < 10^4


def is_pal(n):
    s = str(n)
    size = len(s)//2
    return s[:size] == s[-1:-size-1:-1]

def calc_sum(i):
    return i*(i+1)*(2*i+1) / 6

valid_nums = set([])
for n in range(2,10000):
    for m in range(n-1):
        num = int(calc_sum(n) - calc_sum(m))
        if num < 10**8 and is_pal(num) :
            valid_nums.add(num)

print(sum(valid_nums))
