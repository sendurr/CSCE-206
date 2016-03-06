# Jeremy Abrams
# CSCE 206
# Homework 3 - P5b.py
# February 18 2016

import argparse

parser = argparse.ArgumentParser(description='Computes Rate of Acceleration')
parser.add_argument('-v', type = float, help = "Used to enter v0 value")
parser.add_argument('-t', type = float, help = "Used to enter t value")

try:
	args = parser.parse_args()

except:
	v0=float(input("v0 was not a number. Please enter a number: "))
	t=float(input("t was not a number. Please enter a number: "))
	g = 9.81
	y = v0*t - 0.5*g*t**2
	print (y)

else:
	v0 = args.v
	t = args.t
	g = 9.81
	y = v0 * t - 0.5*g*t**2
	print (y)