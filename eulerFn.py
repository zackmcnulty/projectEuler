def isPrime(n):
    if n <= 1: return False
    if n == 2: return True
    for div in range(2, int(n**(0.5)) + 1):
        if n % div == 0: return False
    return True

