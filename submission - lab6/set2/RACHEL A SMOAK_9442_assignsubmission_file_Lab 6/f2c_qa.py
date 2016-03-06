#Rachel Smoak
#28 February 2016

#Lab 6

#Question 2

# Make a program that reads a temperature in Fahrenheit
# degrees from command line using sys.argv approach; (ii) computes the correspodning
# temperature in Celsius degrees; and (iii) prints out the temperature in
# the Celsius scale. Name of program file: f2c_qa.py

import sys
from math import *
print sys.argv
F = float(sys.argv[-1])
C = (F-32)*5./9.
print "Temperature in degrees Fahrenheit:", sys.argv[-1]
print "Temperature in degrees Celsius:", C
