def minmaxave(numbers):
	maximum=numbers[0]
	for x in numbers[1:]:
		if x>maximum:
			maximum=x
	print(maximum)

	minimum=numbers[0]
	for x in numbers[1:]:
		if x < minimum:
			minimum = x
	print (minimum)

	average = float(sum(numbers))/len(numbers)
	print (float(average))

print (minmaxave([3,5,2.3,5,10,4.2]))