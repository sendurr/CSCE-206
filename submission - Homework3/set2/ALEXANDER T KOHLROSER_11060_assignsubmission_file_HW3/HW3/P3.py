def minmaxave(numbers):
	max = 0
	ave = 0
	min = 10000000
	sum = 0
	count = 0
	for x in numbers:
		if x > max:
			max = x
		if x <= min:
			min = x
		sum = x + sum
		count = count + 1
	ave = sum / count
	print "max = ", max
	print "min = ", min
	print "ave = ", ave

minmaxave([3,5,2,3,5,10,4,2])
