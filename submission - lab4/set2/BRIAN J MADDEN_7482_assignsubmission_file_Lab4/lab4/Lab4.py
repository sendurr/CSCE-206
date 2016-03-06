#Question 1
primes=[2,3,5,7,11,13]
for i in primes:
	print(i)
p=17
primes.append(p)
print(primes)

#Question2

s=0
k=1
M=100
while k < M:
	s+=1/k
	k+=1
print(s)

for i in range(k,M+1):
	s+=1./i
print(s)






#Question 3 
import numpy
M=numpy.matrix([[1,2,3],[4,5,6],[7, 8, 9]])
#column wise sum
M.sum(axis=0)
#row wise sum
M.sum(axis=1)
print(M.sum(axis=0))
print(M.sum(axis=1))



