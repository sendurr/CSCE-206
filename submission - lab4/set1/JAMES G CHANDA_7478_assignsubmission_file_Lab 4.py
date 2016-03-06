#Lab 4 

#Question 1: work with a list
print "*****Question 1: Work with a list*****"

primes = [2,3,5,7,11,13]
for x in primes:
	print x

p=17
primes.append(p)
print primes



#Question 2: Compute a mathematical sum
print "*****Question 2: Compute a mathematical sum*****"
from math import *

#For loop for question 2
s=0; k=1; M=100
for i in range(k,M+1):
	s+=1./i
print "S:", s

#While loop for question 2
s = 0; k = 1.0; M = 100
while k <= M:
    s += 1/k
    k += 1
print "S:", s



#Question 3: Storing a matrix
print "*****Question 3:Storing a matrix*****"

M= [[1,2,3],
[4,5,6],
[7,8,9]]

print sum (map(sum,M))
