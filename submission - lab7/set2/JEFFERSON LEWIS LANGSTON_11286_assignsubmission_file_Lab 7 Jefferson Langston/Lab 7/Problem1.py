import sys

args = sys.argv[1:]

operation = args[0]
num1 = int(args[1])
num2 = int(args[2])

if operation == 'add':
	total = num1 + num2
elif operation == 'subtract':
	total = num1 - num2
elif operation == 'multiply':
	total = num1 * num2
elif operation == 'divide':
	total = num1 / num2

print total



