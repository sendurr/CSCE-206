def sumoddnumber(numbers):
	total = 0
	for i in numbers:
		if i % 2 != 0:
			total += i
	return total

print sumoddnumber([2,5,7,4,8,3,5])