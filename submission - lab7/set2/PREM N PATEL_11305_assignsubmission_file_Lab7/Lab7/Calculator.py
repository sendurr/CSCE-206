import sys

print sys.argv

try:
    val1 = float(sys.argv[2])
    val2 = float(sys.argv[3])
except:
    print "Error: not numerical values"

op = sys.argv[1]

if op == "*":
	print val1*val2
elif op == "**":
	print val1**val2
elif op =="-":
	print val1-val2
elif op == "+":
	print val1+val2
elif op == "/":
	if val2==0:
		print "Error: division by 0"
	else:
		print val1/val2