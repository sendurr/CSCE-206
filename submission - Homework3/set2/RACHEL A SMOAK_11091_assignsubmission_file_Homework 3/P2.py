#Rachel Smoak
#Homework 3
#28 February 2016

#Question 2

def sumoddnumbers(numbers):
	value=0
	for i in numbers:
		if i%2>0: #if i is odd
			value+=i #then add it
		i+=1 #next i
	print "Sum = ", value

sumoddnumbers([2,5,7,4,8,3,5])