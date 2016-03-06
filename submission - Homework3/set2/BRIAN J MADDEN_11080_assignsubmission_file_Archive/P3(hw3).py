import numpy
def minmaxwave(numbers):
	return max(numbers),min(numbers),numpy.mean(numbers)
print(minmaxwave([3,5,2.3,5,10,4.2]))