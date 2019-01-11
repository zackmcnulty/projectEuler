# logic: Clearly, all the bases of our exponents must be less than 10
# as 10^n has more than n digits for any n. This greatly reduces the numbers we have to check.


def get_num_count(n):
    elements = []
    for i in range(1,10):
        if len(str(i**n)) == n: 
            elements.append(i**n)
    return elements 


total = []
for n in range(1, 100):
    total.extend(get_num_count(n))

print(len(total))
