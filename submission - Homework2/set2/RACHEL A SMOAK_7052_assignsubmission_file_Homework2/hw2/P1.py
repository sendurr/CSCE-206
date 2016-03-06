#Rachel Smoak
#Homework 2
#14 February 2016

#Problem 1
#A number series is defined by the following rules. The first two numbers are 0 and 1. And all the following numbers are defined as the sum of previous two numbers. Write a program to generate the first 1000 numbers in this number series with 0, 1 included.
Series = [0,1] #Define first two given numbers
a = Series[-1] #Define variables to last two values
b = Series[-2]
x = 0 #This was an arbitraty definition of x
while len(Series)<1001: #To print the first 1000 number, including 0 and 1
	x = a+b #Add last two numbers
	Series.append(x) #Add sum to list
	a = Series[-1] #Update the values of a and b; without this, it returns only 1s
	b = Series[-2]
print "First 1000 numbers in Fibonacci sequence:", Series

