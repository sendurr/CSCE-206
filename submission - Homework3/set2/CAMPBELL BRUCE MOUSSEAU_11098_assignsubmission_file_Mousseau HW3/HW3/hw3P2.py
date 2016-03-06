import math

def sumoddnumbers(numbers):
	total = 0
	odd = []
	for num in numbers:
		if num not in odd:
			odd.append(num)
		for num in odd:
			if num % 2 == 1:
				total += num
		return total
print ('sum=',sumoddnumbers(numbers=[2,5,7,4,8,3,5]))

