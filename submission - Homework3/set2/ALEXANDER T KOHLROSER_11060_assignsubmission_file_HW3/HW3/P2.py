def sumoddnumber(numbers):
	sum = 0
	for x in numbers:
		if x % 2 != 0:
			sum = x + sum
	print "sum = ", sum

sumoddnumber([2,5,7,4,8,3,5])