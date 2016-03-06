# Name: Lucke Oliveira Luz			Assignment: Homework 3      Exercise: 2

def sumoddnumber(numbers):
	sum_odd = 0
	for i in numbers:
		if i%2 != 0:
			sum_odd += i
	return sum_odd

print "sum =", sumoddnumber([2,5,7,4,8,3,5])

# THE PROBLEM SUGGESTS A RESULT OF 15 FOR THE SUM, BUT FOR THE GIVEN LIST THE CORRECT IS A RESULT OF 20 ---> 5+7+3+5