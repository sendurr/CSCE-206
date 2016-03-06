def sumoddnumber(numbers):
	total = 0
	for n in numbers:
		if n%2==1:
			total+=n
	print total

numbers = (2, 5, 7, 4, 8, 3, 5)

print sumoddnumber(numbers)