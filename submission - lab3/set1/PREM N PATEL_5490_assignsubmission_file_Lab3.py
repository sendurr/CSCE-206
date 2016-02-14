# LAB 3

print "Problem 1:"
L1 = [2, 3, 4, 10]
L2 = [5, 3, 4, 9, 10, 15]
print set(L1) & set(L2)
print set(L1) | set(L2)
print set(L1) - set(L2)
L3 = L1 + L2; print L3
L2.append(103); L2.append(20); L2.append(34)
print L2

print "----------------------------------------------\nProblem 2:"
# print sum(range(13,1000,2))
sum1 = range(13,1000,2)
sum = 0
i = 0
while i < len(sum1):
	sum += sum1[i]
	i += 1
print sum

print "----------------------------------------------\nProblem 3:"
import random
x = [int(300*random.random()) for i in xrange(300)]
multiples = []
i=0
while i < len(x):
	if x[i]%3==0 & x[i]%7==0:
		multiples.append(x[i])
	i+=1
print multiples
print 