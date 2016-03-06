def sumoddnumber(numbers):
	total = 0
	for num in numbers:
		if num % 2 == 1:
			total += num
	return total

print "sum =", sumoddnumber([2,5,7,4,8,3,5])	#Sum of odd numbers in this list = 20