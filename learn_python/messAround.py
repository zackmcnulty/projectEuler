import random as r
import time
import math
#messing with map(func, list1,list2, ...)

x = list([1,2,3,4,5])
y = list([1,3,3])
print x < y
x = x * 4
print x

fn = lambda x,y: 3*x**2 + y


func = lambda input1, input2: input1 * math.exp(input2)

xs = list([1,2,3,4,5,6])
ys = list([4,5,6,19,1,2])
print map(fn, xs, ys)
# uses first list as elements for first parameter in function,
# and second list for second parameter

#messing with filter (func, list) *returns values in list that func evaluates to true

evens = filter(lambda x: x%2 == 0, [1,2,3,4,5,6,7,8,9,10])
print evens


oddProducts = filter(lambda x: x % 2 == 1, map(lambda x,y: x*y, [1,2,3,4,5,6,7,9,10], [1,2,3,5,5,5,5,5,5]))
print "oddProducts: " + str(oddProducts)


# messing with reduce(func, list)
# *returns single value: removes first 2 elements of list, applies func to them, and puts returned
# value at from of list; continues process until only one remains
maxOfTwo = lambda x,y: max(x,y)
list1 = list([1,2,3,4,5,5,5,19,23,3,43,1,2,3,4,5,6,10])
max = reduce(maxOfTwo, list1)
print max


time.sleep(1000)

a = [x**2 for x in range(1,11)]
b = [a[2*i] for i in range(0, len(a)/2)]
for i,k in enumerate(a):
    print str(i) + ", " + str(k)
print b

list1 = set([r.randint(0,10) for x in range(r.randint(10,20))])
list2 = set([r.randint(0,10) for x in range(r.randint(10,20))])


print list1
print list2
print list1.intersection(list2)

sum = 0
for i in range(0,10):
    sum += i
# sum = 0 + 1 + 2 + ... + 9

l = list([[1,2], [3,4], [5,6]])
for x,y in l:
    print "(" + str(x) + ", " + str(y) + ")"

tuple(1,2,3)

