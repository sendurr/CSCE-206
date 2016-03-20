''' Question 1'''

print "Question 1:"


import sys

args = sys.argv[1:]

op = args[0]
x = int(args[1])
y = int(args[2])

if op == '+':
	total = x + y
elif op == '-':
	total = x - y
elif op == '*':
	total = x * y
elif op == '/':
	if y == 0:
		print "error: y = 0"
	else:
		total = x / y

print total


