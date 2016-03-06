#Rachel Smoak
#28 February 2016

#Lab 6

#Question 3

# Make a program that reads a temperature in Fahrenheit
# Degree or Celsius degree from command line using argparse module and convert to
#Celsius or Fahrenheit correspondingly. The program should be able to run as below
# input -f/c number

import argparse
import sys
parser = argparse.ArgumentParser(description = "Convert temperatures between Fahrenheit and Celsius")
parser.add_argument('-f', action = 'store', dest = 'tempf', default = None)
parser.add_argument('-c', action = 'store', dest = 'tempc', default = None)
if len(sys.argv) > 2:
	args = parser.parse_args()
	if args.tempf is None and args.tempc is None:
		print "Improper input, see help"
	elif args.tempc is not None:
		try:
			C = float(args.tempc)
			F = 9./5.*C+32 
			print "Input: ", "%.2f" %C, "degrees(C)"
			print "Output: ", "%.2f" %F, "degrees(F)"
		except:
			print "Improper input, see help"	
	elif args.tempf is not None:
		try:
			F = float(args.tempf)
			C = (F-32)*5./9.
			print "Input: ", "%.2f" %F, "degrees(F)"
			print "Output: ", "%.2f" %C, "degrees(C)"
		except:
			print "Improper input, see help"
	else:
		#This is the case where both args.tempf and args.tempc are not None.
		print "Improper input, see help"
else:
	print "Improper input, see help"