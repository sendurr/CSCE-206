'''Question 3'''


import argparse
import sys

parser = argparse.ArgumentParser(description = "converts temperature")
parser.add_argument ("temperature", type = float, help = "input temperature")
parser.add_argument ("--F", "--Fahrenheit", action = "store_true", help = "degrees F")
parser.add_argument ("--C", "--Celcius", action = "store_true", help = "degrees C")
args = parser.parse_args()

AnswerC= (args.temperature*9.0/5.0)+32
AnswerF= (args.temperature-32.)*5.0/9.

if args.celcius:
	print "degrees celcius: %.2f"% (args.temperature)
	print "degrees fahrenheit = %.2f"% (AnswerC)

if args.fahrenheit:
	print "degrees fahreneit = %.2f" % (args.temperature)
	print "degrees celcius = %.2f"%(AnswerF)


