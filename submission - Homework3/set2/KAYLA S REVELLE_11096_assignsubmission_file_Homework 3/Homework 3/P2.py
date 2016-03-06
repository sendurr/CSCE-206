def sumoddnumber(numbers):
	x = 0
	for i in numbers:
		if i%2==1:
			x+=i
	print(x)

print (sumoddnumber([2,5,7,4,8,3,5]))