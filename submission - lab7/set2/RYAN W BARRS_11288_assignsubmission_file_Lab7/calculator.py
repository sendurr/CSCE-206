import sys
x = float(sys.argv[2])
y = float(sys.argv[3])

operator=sys.argv[1]
if operator == "+":
	print x + y
elif operator == "-":
	print x - y
elif operator == "*":
	print x * y
elif operator == "/":
	if y==0:
		print "Error: denominator cannot equal 0"
	else:
		print x/y