import sys
from math import *
print sys.argv
x=float(sys.argv[2])
print x
y=float(sys.argv[3])
print y

ops=sys.argv[1]
print x,ops,y,'='
if ops== "+":
	print x+y
elif ops== "*":
	print x*y
elif ops=="-":
	print x-y
elif ops== "/":
	if y ==0:
		print "error: denominator cannot be 0"
	else:
		print x/y
