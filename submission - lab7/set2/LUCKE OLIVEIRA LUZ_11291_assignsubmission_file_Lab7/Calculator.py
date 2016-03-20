import sys

op = str(sys.argv[1])
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if op == "+":
	print num1 + num2
elif op == "-":
	print num1 - num2
elif op == "*":
	print num1 * num2
elif op == "/":
	if num2 == 0:
		print "DENOMINATOR CANNOT BE ZERO"
	else:
		print num1 / num2