'''Question 2: Take input from command line using sys.argv'''


def FtoC(F):
	return (F-32)*5.0/9.0

import sys
print "Fahrenheit = %s in Celsius = %d" % (sys.argv[1], FtoC(int(sys.argv[1])))