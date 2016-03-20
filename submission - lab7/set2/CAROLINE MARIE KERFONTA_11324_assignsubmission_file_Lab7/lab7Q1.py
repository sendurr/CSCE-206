import sys
print (sys.argv)
x= float(sys.argv[1])
y= float(sys.argv[3])


op=sys.argv[2]
if op == "+":
	print (x, "+", y, "=", x+y)
elif op == "-":
	print (x, "-", y, "+", x-y)
elif op == "*":
	print (x, "*", y, "=", x*y)
elif op == "/" :
	if sys.argv[3] == 0:
		print ("ERROR: denominator cannot be 0")
	elif op == "/":
		print (x, "/", y, "=", x/y)