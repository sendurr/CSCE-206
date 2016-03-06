#1
primes = [2,3,5,7,11,13]
for i in primes:
	print i
p = 17
primes.append(p)
print primes


#2
k = 1
s = 0
M = 20
while k <= M:
	k += 1
	s += 1.0/k
print "while loop:", s

k = 1
s = 0
M = 20
for k in range(1, M+1):
	s += 1.0/k
print "for loop:", s


#3
import numpy
M = numpy.matrix([[1,2,3],[4,5,6,],[7,8,9,]])
print "Column sum:", M.sum(axis=0)
print "Row sum:", M.sum(axis=1)