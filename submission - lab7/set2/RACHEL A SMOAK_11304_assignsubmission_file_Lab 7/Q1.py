#Rachel Smoak
#Lab 7
#6 March 2016

#Question 1

import sys
import operator
from math import *

n = float(sys.argv[2])
p = float(sys.argv[-1])

ops = {"+":operator.add, "-":operator.sub,"*":operator.mul, "/": operator.div}
op_char = sys.argv[1]
op_func = ops[op_char]
if p==0:
	print "Error: denominator cannot be 0"
else:
	result = op_func(n,p)
	print sys.argv[2],op_char,sys.argv[-1], "= ", result