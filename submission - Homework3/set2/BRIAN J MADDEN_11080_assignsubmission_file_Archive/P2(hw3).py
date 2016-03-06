def sumoddnumber(numbers):
	total=0
	for x in numbers:
		if x % 2 == 1:
			total+=x
	return total
print("Sum=", sumoddnumber([2,5,7,4,8,3,5]))	