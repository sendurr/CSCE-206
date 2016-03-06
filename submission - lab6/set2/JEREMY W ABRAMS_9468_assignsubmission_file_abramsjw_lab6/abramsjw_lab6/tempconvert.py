# Jeremy Abrams
# CSCE 206
# Lab 6 - tempconvert.py
# February 11, 2016

import argparse


parser = argparse.ArgumentParser(description='Converts between Fahrenheit and Celcius.')
parser.add_argument('-f', type = float, help="Used to enter a temperature in Fahrenheit.")
parser.add_argument('-c', type = float, help="Used to enter a temperature in Celsius")

args = parser.parse_args()

if(args.f is not None):
	print ("The temperature in Fahrenheit is: ", args.f)
	celsius = (args.f - 32) * (5/9)
	print ("The temperature in Celsius is: ", celsius)

if(args.c is not None):
	print ("The temperature in Celsius is: ", args.c)
	fahrenheit = (args.c * (9/5)) + 32
	print ("The temperature in Fahrenheit is: ", fahrenheit)