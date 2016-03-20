from numpy import *
form matplotlib.pylab import *
import sys
def multiply(x,y):
	a=x*y
	return a

def add(x,y):
	b=x+y
	return b

def divide(x,y):
	c=float(x)/y
	return c
def subtract(x,y):
	d=x-y
	return d

x=float(sys.argv[2])
y=float(sys.argv[3])

if sys.argv[1]=="*":
	print(multiply(x,y))
if sys.argv[1]=="/":
	if y=0:
		print("Error: divide by zero")
	else:
		print(divide(x,y))



