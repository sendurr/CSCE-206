def minmaxave(numbers):
	average = sum(numbers)/float(len(numbers))
	minimum = min(numbers)
	maximum = max(numbers)
	return('Average = %.1f'%average,'Minimum = %.1f'%minimum,'Maximum = %.1f'%maximum)

print(minmaxave([3,5,2.3,5,10,4.2]))