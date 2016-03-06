

oddnumber = []
def sumoddnumber(*arg):
	for number in sumoddnumber:
		if number%2 != 0:
			oddnumber.append(number)
		else:
			pass
	print "sum =", sum(oddnumber)

print sumoddnumber([2,5,7,4,8,3,5])

# I keep getting function object is not iterable
# but I cant figure out how to get the bug fixed