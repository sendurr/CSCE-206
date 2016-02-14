#1
L1 = {2,3,4,10}
L2 = {5,3,4,9,10,15}

print L1 & L2
print (L1 | L2) - (L1 & L2)
print L1 - L2

L2 = list(L2)
L3 = (103,20,34)
L2.append(L3)
print L2

#2
x = 13
stepsize = 2
x_sum = 0
while x<999:
	x_sum += x
	x += stepsize
print x_sum

#3
import random
x=[int(300*random.random()) for i in xrange(300)]
#print x
index = 0
while index < 300:
	if x[index]%3==0 and x[index]%7==0:
		print x[index]
	index += 1

