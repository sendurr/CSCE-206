# Jeremy Abrams
# CSCE 206
# Homework 3 - P3.py
# February 18 2016

def minmaxave(numbers):
	minval = 100
	maxval = 0
	average = 0

	for number in numbers:
		if number < minval:
			minval = number
		if number > maxval:
			maxval = number
		average = average + number

	average = average / len(numbers)

	return "Minimum: ",minval, "Maximum: ", maxval, "Average: ", average

print minmaxave([3,5,2.3,5,10,4.2])