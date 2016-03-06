import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='F', default=None, help='Fahrenheit')
parser.add_argument('-c', action='store', dest='C', default=None, help='Celsius')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

if args.F is not None:
	tempC = (float(args.F)-32)*(5/9.0)
	print "deg(F) = %f\ndeg(C) = %f"%(float(args.F), tempC)
elif args.C is not None:
	tempF = ((9/5.0)*float(args.C))+32
	print "deg(C) = %f\ndeg(F) = %f"%(float(args.C), tempF)