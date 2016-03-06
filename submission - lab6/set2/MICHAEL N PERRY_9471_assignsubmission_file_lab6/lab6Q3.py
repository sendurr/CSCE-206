#lab 6 Question 3
import argparse
import sys
parser=argparse.ArgumentParser(description="converts temperature")
parser.add_argument("temp",type=float,help="inputed temperature")
parser.add_argument("-f","--Fahrenheit",action="store_true",help="degree in Fahrenheit")
parser.add_argument("-c","--Celsius",action="store_true",help="degree in Celsius")
args=parser.parse_args()
answer1=(args.temp-32)*5.0/9.0
answer2=(args.temp*9.0/5.0)+32.0
if args.Fahrenheit:
	print "input: {} degree(F)".format(args.temp)
	print "output: {:.4} degree(C)".format(answer1)
if args.Celsius:	
	print "input: {} degree(C) ".format(args.temp)
	print "output: {:.4} degree(F)".format(answer2)