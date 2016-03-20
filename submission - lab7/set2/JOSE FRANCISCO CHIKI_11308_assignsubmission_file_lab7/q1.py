import sys
print sys.argv
x=float(sys.argv[2])
print x
y=float(sys.argv[3])
print y
op=sys.argv[1]
if op=="+":
	print x+y
elif op=="*":
	print x*y
elif op=="/":
	if y==0:
		print "error, y=0"
	else:
		print x/y
elif op=="-":
	print x-y
print x,op,y,'=',