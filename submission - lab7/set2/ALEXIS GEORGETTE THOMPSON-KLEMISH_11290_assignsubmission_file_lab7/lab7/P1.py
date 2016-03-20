from sys import argv
operator = argv[1]
first = float(argv[2])
second = float(argv[3])

if operator == '+':
	value = first + second
	print value
elif operator == '-':
	value = first - second
	print value
elif operator == '*':
	value = first * second
	print value
elif operator == '/':
	try: 
		value = first / second
		print value
	except:
		print "denominator cannot be 0"

