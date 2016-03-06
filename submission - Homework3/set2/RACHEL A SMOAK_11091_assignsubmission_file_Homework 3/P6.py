#Rachel Smoak
#Homework 3
#28 February 2016

#Question 6
import sys
import argparse


parser = argparse.ArgumentParser(description = "Find the y-position of an object with gravitational acceleration.")
parser.add_argument('-v', action='store', dest='v0list', default=None, help='Initial velocity in m/s')
parser.add_argument('-t', action='store', dest='tlist',default=None, help='Time in seconds')
try: #if either or both of the inputs are empty
	args = parser.parse_args()
	try: #if the time input is not a number
		try:
			t = float(args.tlist)
		except:
			t = float(raw_input("Please re-enter correct time input (t = ? s): "))
		try: #if the velocity input is not a number
			v0 = float(args.v0list)
		except:
			v0 = float(raw_input("Please re-enter correct velocity input (v0 = ? m/s): "))
		g = 9.81
		y = v0*t-0.5*g*t**2
		print "Position at v0 = ", v0, "and t = ", t, "is", y
	except: #hopefully everything is caught by now, so just exit
		sys.exit(0)
except: #if all of the arguments are not correctly defined, this should ask for new input and run
	t = float(raw_input("Please re-enter correct time input: t = ? s "))
	v0 = float(raw_input("Please re-enter correct velocity input: v0 = ? m/s "))
	g = 9.81
	y = v0*t-0.5*g*t**2
	print "Position at v0 = ", v0, "and t = ", t, "is", y