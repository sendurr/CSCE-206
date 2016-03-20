import sys
args = sys.argv[1:]

program = args[0]
number1 = int(args[1])
number2 = int(args[2])

if program == 'add':
	total = number1 + number2
elif program == 'subtract':
	total = number1 - number2
elif program == 'multiply':
	total = number1 * number2
elif program == 'divide':
	total = number1 / number2
	if number2 = 0 in 'divide':
		total = 'Error' 


print (total)

