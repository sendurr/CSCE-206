print "Lab 6 - Question 3"
print ""

import argparse
import sys

parser = argparse.ArgumentParser(description="Converts Temperature")
parser.add_argument("Temperature", type=float, help="Input Temperature")
parser.add_argument("-F", "--Fahrenheit", action="store_true", help="Degrees Fahrenheit")
parser.add_argument("-C", "--Celsius", action="store_true", help="Degrees Celsius")
args=parser.parse_args()

AnswerOne=(args.Temperature-32.0)*5.0/9.0
AnswerTwo=(args.Temperature*9.0/5.0)+32.0

if args.Fahrenheit:
	print "Degrees Fahrenheit: %.2f"%(args.Temperature)
	print "Degrees Celsius: %.2f"%(AnswerOne)
if args.Celsius:
	print "Degrees Celsius: %.2f"%(args.Temperature)
	print "Degrees Fahrenheit: %.2f"%(AnswerTwo)

print ""