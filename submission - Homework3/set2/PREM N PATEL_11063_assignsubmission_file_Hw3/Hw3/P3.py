def minmaxave(numbers):
	total = 0
	for i in numbers:
		total += i
	maximum = max(numbers)
	minimum = min(numbers)
	mean = total/float(len(numbers))
	return "Max = ", maximum, "Min = ", minimum, "Mean = ", mean

print minmaxave([3,5,2,3,5,10,4.2])