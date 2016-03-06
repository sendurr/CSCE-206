def sumoddnumber(numbers):
	total=0
	for x in numbers:
		if x%2 == 0:
			continue
		else:
			total += x
	return total
print "sum =", sumoddnumber([2,5,7,4,8,3,5])