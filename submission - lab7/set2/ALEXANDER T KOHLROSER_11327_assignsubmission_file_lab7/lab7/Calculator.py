from sys import argv

operand = argv[1]

number1 = float(argv[2])

number2 = float(argv[3])

answer = 0.0
#sets variables
if operand == "+":
	answer = number1 + number2
	print answer
#plus
elif operand == "-":
	answer = number1 - number2
	print answer
#minus
elif operand == "*":
	answer = number1 * number2
	print answer
#multiply
elif operand == "/":
	try:
		answer = number1 / number2
		print answer
	except:
		print "denominator cannot be 0"
#divide that checks for /0 error and notifies user if that has happened