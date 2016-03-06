import sys
from math import *

def C(F):
	C=(F-32.0)*(float(5)/9.0)
	print ("%.2f"%C)

#print (sys.argv)

F=float(sys.argv[1])

print (C(F))