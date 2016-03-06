# Jeremy Abrams
# CSCE 206
# Homework 3 - P2.py
# February 18 2016

def sumoddnumber(numbers):
	total = 0
	for number in numbers:
		if number%2 != 0:
			total = total + number

	return total


print ("sum=", sumoddnumber([2,5,7,4,8,3,5]))