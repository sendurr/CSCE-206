import math

def sumoddnumbers(numbers):
	total = 0
	s = []
	for num in numbers:
		if num not in s:
			s.append(num)
	for num in s:
		if num % 2 == 1:
			total += num
	return total 

if __name__ == '__main__':
	print 'sum =',sumoddnumbers(numbers=[2,5,7,4,8,3,5])



