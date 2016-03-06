#Rachel Smoak
#14 Fenruary 2016

#Question 1
print "Question 1"
print "Each list element:"
i = 0
primes = [2,3,5,7,11,13]
for i in primes:
	print i
	i+=1
p = 17
primes.append(p)
print "Primes with p appended:",primes

#Question 2
print "--------------------------------------------------"
print "Question 2"
M=10
k = range(1,M+1)
forsummation = 0
for i in k:
	q = 1./i
	forsummation+=q
	i+=1
print "For loop summation=",forsummation
x=0
whilesummation = 0
while x<len(k):
	q = 1./k[x]
	whilesummation+=q
	x+=1
print "While loop summation=",whilesummation

import numpy as np
#Question 3
print "--------------------------------------------------"
print "Question 3"
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
Msum = np.sum(M)-M[1][1]
print "Sum of all boundary numbers = %d" %Msum