# Jeremy Abrams
# CSCE 206
# Lab 7 - Calculator.py
# February 25, 2016

import sys

op = sys.argv[1]
x = float(sys.argv[2])
y = float(sys.argv[3])

if op=="+":
	print (x,"+",y,"=",(x+y))
elif op=="-":
	print (x,"-",y,"=",(x-y))

elif op=="/":
	if(y == 0):
		print("error: denominator cannot be 0")
	else:
		print (x,"/",y,"=",(x/y))
elif op=="*":
	print (x,"*",y,"=",(x*y))
