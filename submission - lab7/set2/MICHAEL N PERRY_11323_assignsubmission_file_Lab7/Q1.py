#Q1
import sys

x=float(sys.argv[2])
y=float(sys.argv[3])
op=sys.argv[1]

print x,op,y,'=',
 
if op == "*":
    print x*y
elif op =="-":
    print x-y
elif op == "+":
    print x+y
elif op == "/":
    if y==0:
        print "error: denominator cannot be 0"
    else:
        print x/y