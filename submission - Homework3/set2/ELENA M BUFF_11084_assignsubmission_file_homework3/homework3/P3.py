def minmaxave(numbers):
	start=0
	for x in numbers:
		start+=x
		average=start/len(numbers)
	print "minumum value= ", min (numbers)
	print "maxiumum value= ", max (numbers)
	return "average= " "%.3f"%average

print minmaxave([3,5,2.3,5,10,4.2])