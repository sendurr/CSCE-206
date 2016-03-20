# Question 1--------------------
import sys
import argparse

op=str(sys.argv[1])
x=eval(sys.argv[2])
y=eval(sys.argv[3])

print(x,op,y,'=',)

if op == "*":
	print(x*y)
elif op =="-":
	print(x-y)
elif op == "+":
	print(x+y)
elif op == "/":
	if y==0:
		print("error: y=0")
	else:
		print(x/y)
