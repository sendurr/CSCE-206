# Name: Lucke Oliveira Luz         Assignment: Lab 6         Exercise: 3

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-F', action='store', dest='F',default=0, help='Temperature in Fahrenheit')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

F = args.F
F = float(F)
C = (5/9.0)*(F - 32)
print "Temperature in Celsius is %.2f degrees"% (C)