# logic: simply work in modulo to avoid dealing with that massive number.
# If we want the final 10 digits, simply perform operations mod 10**10



digits = 28433

for _ in range(7830457):
    digits = (digits * 2) % (10**10)

digits += 1
print(digits)
