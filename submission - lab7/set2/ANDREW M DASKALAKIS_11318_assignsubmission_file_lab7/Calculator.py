from math import *
import sys

o = sys.argv[1]
x = sys.argv[2]
y = sys.argv[3]

if o == "*":
	try:
		z = float(x)*float(y)
		print x+o+y+ "=%0.2f" %(z)
	except:
		print "The first value must be an operator, followed by two numbers"
elif o == "+":
	try:
		z = float(x)+float(y)
		print x+o+y+ "=%0.2f" %(z)
	except:
		print "The first value must be an operator, followed by two numbers"
elif o == "-":
	try:
		z = float(x)-float(y)
		print x+o+y+ "=%0.2f" %(z)
	except:
		print "The first value must be an operator, followed by two numbers"
elif o == "/":
	try:
		z = float(x)/float(y)
		print x+o+y+ "=%0.2f" %(z)
	except:
		print "The first value must be an operator, followed by two numbers. Also the denomonator cannot be 0"
