import sys

x=int(sys.argv[2])
y=int(sys.argv[3])

op=sys.argv[1]
print x,op,y,'='

if op == "+":
	print x+y
elif op == "*":
	print x*y
elif op == "-":
	print x-y
elif op == "/":
	if y==0:
		print "Error: denominator cannot be 0"
	else:
		print x/y