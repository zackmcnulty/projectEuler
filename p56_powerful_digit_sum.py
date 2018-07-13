# correct!

def digitSum(n):
    if n == 0:
        return 0
    else:
        return n%10 + digitSum(n/10)

nums = [a**b for a in range(1,100) for b in range(1,100)]

maxSum = 0
for n in nums:
    maxSum = max(maxSum, digitSum(n))

print maxSum