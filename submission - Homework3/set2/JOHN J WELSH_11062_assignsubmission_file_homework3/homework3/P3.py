def minmaxave(numbers):
	maximum = max(numbers)
	minimum = min(numbers)
	average = sum(numbers)/len(numbers)
	return maximum,minimum,average

print minmaxave([3,5,2.3,5,10,4.2])