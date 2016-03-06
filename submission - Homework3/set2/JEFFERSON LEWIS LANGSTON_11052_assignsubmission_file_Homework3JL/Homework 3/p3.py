import numpy

def minmaxave(numbers):
	minimum = min(numbers)
	maximum = max(numbers)
	average = numpy.mean(numbers)
	return minimum, maximum, average
print minmaxave([3,5,2.3,5,10,4.2])



