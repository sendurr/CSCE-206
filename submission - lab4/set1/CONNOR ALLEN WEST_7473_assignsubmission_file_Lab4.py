#1
primes = [2,3,5,7,11,13]
for i in primes:
	print(i)
p=17
primes.append(p)
print(primes)

#2
k=1
M=42
s=0
for i in range(k,M):
	s+=(1/i)
print(s)

s=0
while k<M:
	s+=(1/k)
	k=k+1
print(s)

#3
import numpy
M = numpy.matrix('1 2 3; 4 5 6; 7 8 9')
TOTAL=(numpy.sum(M))-(M[1,1])
print(TOTAL)