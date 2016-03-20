from sys import argv

op, num1, num2 = argv[1], float(argv[2]), float(argv[3])

if op == '*':
	answer = num1 * num2
	print answer
elif op == '+':
	answer = num1 + num2
	print answer
elif op == '-':
	answer = num1 - num2
	print answer
elif op == '/':
	try: 
		answer = num1 / num2
		print answer
	except:
		print "denominator cannot be 0"
