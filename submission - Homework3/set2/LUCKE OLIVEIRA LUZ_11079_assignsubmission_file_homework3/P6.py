# Name: Lucke Oliveira Luz			Assignment: Homework 3      Exercise: 6

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v0', action='store', dest='v0',default=0, help='Initial velocity')                            
parser.add_argument('-t', action='store', dest='t',default=0, help='Time')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

try:
	v0 = float(args.v0)
	t = float(args.t)
	g = 9.81
	y = v0*t - 0.5*g*t**2
	print y
except:
	print "'v0' AND 't' MUST BE NUMBERS"