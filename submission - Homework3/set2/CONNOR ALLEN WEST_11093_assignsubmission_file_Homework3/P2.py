def sumoddnumber(numbers):
	even = 0
	for x in numbers:
		if x%2==0:
			even+=x
	grandtot = sum(numbers)
	total = (grandtot-even)
	print('Sum = %d'%total)

sumoddnumber([2,5,7,4,8,3,5])