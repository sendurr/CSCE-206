#1
L1=[2,3,4,10]
L2=[5,3,4,9,10,15]
 both=set(L1).intersection(L2)
print both

for element in L1:
    if element not in L2:
        print element

for item in L2:
	if item not in L1:
		print item

L1.extend(L2)
L3 = sorted(L1)
print L3

add={
	L2.append(103)
	L2.append(20)
	L2.append(34)
}
print add

#2
numbers=range(13,999)

def addOddNumbers(numbers):
    for num in numbers:
        if num % 2 == 1:
            return sum
        print sum(numbers)

#3

import random
x=[int(300*random.random()) for i in xrange(300)]

random.random(300)
print 

from random import
x=[int(300*random.random(3,7)) for i in xrange(300)]