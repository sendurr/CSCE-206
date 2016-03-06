def sum_odd(integers):
	odds = []
	for i in integers:
		if i%2!=0:
			odds.append(i)
	return sum(odds)

print sum_odd([2,5,7,4,3,5])
