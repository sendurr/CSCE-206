#P1: A number series is defined by the following rules. 
#he first two numbers are 0 and 1. And all the following numbers 
#are defined as the sum of previous two numbers. Write a program 
#to generate the frst 1000 numbers in this number series with 0, 1 included.

def numberseries(n):
	a=0
	b=1
	for i in range (0,n):
		print (a)

		num = a
		a= b
		b=num + b
	return a

print numberseries(1000)

