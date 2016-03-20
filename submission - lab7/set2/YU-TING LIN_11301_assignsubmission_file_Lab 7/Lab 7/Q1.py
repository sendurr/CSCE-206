import sys

print sys.argv
x= float(sys.argv[1])
y=float(sys.argv[3])

op=sys.argv[2]
print x,op,y,'=',

if op =="-":
	print x-y
elif op == "+":
	print x+y
elif op == "*":
	print x*y
elif op == "/":
	if y==0:
		print "error: y=0"
	else:
		print x/y

