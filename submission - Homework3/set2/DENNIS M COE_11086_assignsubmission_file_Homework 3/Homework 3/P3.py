def minmaxave(numbers):
	max_elem = numbers[0]
	for e in numbers[1:]:
		if e > max_elem:
			max_elem = e
	print max_elem

	minimum = numbers[0]
	for e in numbers[1:]:
		if e < minimum:
			minimum = e
	print minimum

	ave=float(sum(numbers))/len(numbers)
	print float(ave)

numbers = (3, 5, 2.3, 5, 10, 4.2)

print minmaxave(numbers)