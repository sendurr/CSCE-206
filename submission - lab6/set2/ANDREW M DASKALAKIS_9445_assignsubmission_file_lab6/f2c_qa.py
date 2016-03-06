from math import *
import sys

Tf = float(sys.argv[1])

Tc = (Tf-32)*(5.0/9)

print "Temperature = %0.2f degrees Celsius" %(Tc) 