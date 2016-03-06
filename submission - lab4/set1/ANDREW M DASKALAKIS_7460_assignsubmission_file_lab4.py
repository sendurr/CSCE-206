from math import *
from numpy import *

print "###################################"
print "Problem 1"
print "###################################"
print ""
primes = [2,3,5,7,11,13]

for x in primes:
	print x

p = 17
primes.append(p)



for x in primes:
	print x


print ""
print "###################################"
print "Probem 2"
print "###################################"
print ""

def sum1(M):
	s = 0
	for k in range(1,M+1):
		s += (1.0/k)
	print s

sum1(4)

def sum2(M):
	s = 0
	count = 1
	while count <= M:
		s += (1.0/count)
		count += 1
	print s

sum2(4)


print ""
print "###################################"
print "Problem 3"
print "###################################"
print ""

M = [[1,2,3],[4,5,6],[7,8,9]]
x = 0

for i in range(0,len(M)):
	for j in range(0,len(M)):
		if i == 0 or i == len(M)-1 or j == 0 or j == len(M)-1:
			x += M[i][j]

print x