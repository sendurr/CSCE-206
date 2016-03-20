''' Write a calculator program that accepts commands from the commmand line. 
The program has the following function when executed'''

# def add(x, y):
# 	return x + y

# def subtract(x, y):
# 	return x-y

# def multiply(x, y):
# 	return x*y

# def divide (x,y):
# 	return x/y
		


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# import sys

# choice = raw_input("Enter choice(1/2/3/4):")

# num1 = int(raw_input("Enter first number: "))
# num2 = int(raw_input("Enter second number: "))

# if choice == '1':
#    print(num1,"+",num2,"=", add(num1,num2))

# elif choice == '2':
#    print(num1,"-",num2,"=", subtract(num1,num2))

# elif choice == '3':
#    print(num1,"*",num2,"=", multiply(num1,num2))

# elif choice == '4':
#    print(num1,"/",num2,"=", divide(num1,num2))
# else:
#    print("Invalid input")

import sys

args = sys.argv[1:]

operation = args[0]
x = int(args[1])
y = int(args[2])

if operation == '+':
	total = x + y
elif operation == '-':
	total = x - y
elif operation == '*':
	total = x * y
elif operation == '/':
	if y == 0:
		print "error: y = 0"
	else:
		total = x / y

print total


# import sys

# args = sys.argv

# x=eval(args.x)
# y=eval(args.y)
# op=args.op

# print x,op,y,'=',

# if op == "*":
# 	print x*y
# elif op =="-":
# 	print x-y
# elif op == "+":
# 	print x+y
# elif op == "/":
# 	if y==0:
# 		print "error: y=0"
# 	else:
# 		print x/y