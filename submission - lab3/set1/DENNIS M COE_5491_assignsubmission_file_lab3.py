L1 = [2, 3, 4, 10]
L2 = [5, 3, 4, 9, 10, 15]


print set(L1) & set(L2)
print set(L1) | set(L2)
print set(L1) - set(L2)

L3 = set(L1) | set(L2)
L2.append([103, 20, 34])
print L2


d = range(13, 1000, 2)
sum1 = sum(d)
print (sum1)


import random
numbers = [int(300*random.random()) for i in xrange(300)]

i = 1
while i < len(numbers):
	if numbers[i]%7==0 and numbers[i]%3==0:
		print numbers[i]
	i+=1
	



