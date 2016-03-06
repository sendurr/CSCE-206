#Rachel Smoak
#Homework 3
#28 February 2016

#Question 5
import sys
import argparse

parser = argparse.ArgumentParser(description = "Find the y-position of an object with gravitational acceleration.")
parser.add_argument('-v', action='store', dest='v0list', default=None, help='Initial velocity in m/s')
parser.add_argument('-t', action='store', dest='tlist',default=None, help='Time in seconds')
if len(sys.argv) == 5: #this should only accept input if t and v0 are defined
	args = parser.parse_args()
	try:
		try:
			t = float(args.tlist) #see if t is numeric
		except:
			print "Error: please specify a numeric time t"
			sys.exit(0)
		try:
			v0 = float(args.v0list) #see if v0 is numeric
		except:
			print "Error: please specify a numeric initial velocity v0"
			sys.exit(0)
		g = 9.81
		y = v0*t-0.5*g*t**2
		print "Position at v0 = ", v0, "and t = ", t, "is", y
	except:
		sys.exit(0)
else:
	print "Error: please assign v0 and t values"