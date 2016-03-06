def sumoddnumber(numbers):
	start=0
	for x in numbers:
		if not (x % 2 == 0):
			start+=x
	return start

print "sum=", sumoddnumber([2,5,7,4,8,3,5])