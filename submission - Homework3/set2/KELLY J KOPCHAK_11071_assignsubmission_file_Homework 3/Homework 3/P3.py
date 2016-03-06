def minmaxave(numbers):
	maximum=numbers[0]
	for i in numbers:
		if i>maximum:
			maximum=i
	print "max=",maximum

	minimum=numbers[0]
	for i in numbers:
		if i<minimum:
			minimum=i
	print "min=",minimum

	avg=float(sum(numbers)/len(numbers))
	print "average=",avg
numbers=[3,5,2.3,5,10,4.2]
print minmaxave(numbers)