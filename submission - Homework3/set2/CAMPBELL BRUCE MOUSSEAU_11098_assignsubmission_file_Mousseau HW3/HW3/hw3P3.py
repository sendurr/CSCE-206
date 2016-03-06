import numpy
def minmaxave(numbers):
	m=min(numbers)
	M=max(numbers)
	a=numpy.mean(numbers)
	return m, M, a

print (minmaxave([3,5,2.3,5,10,4.2]))