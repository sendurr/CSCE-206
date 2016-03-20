
# Question 1


import sys
from math import *

print sys.argv
x=float(sys.argv[1])
print x
y=float(sys.argv[3])
print y

op=sys.argv[2]
print x,op,y,'=',

if op == "+":
	print x+y
elif op == "-":
	print x-y
elif op == "*":
	print x*y
elif op == '/':
	if y == 0:
		print "error: y = 0"
	else:
		total = x / y

print total


