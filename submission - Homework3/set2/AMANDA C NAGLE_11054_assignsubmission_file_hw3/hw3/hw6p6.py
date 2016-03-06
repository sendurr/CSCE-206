import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action= 'store')
parser.add_argument('-v', action= 'store')

args = parser.parse_args()
try:
	t=float(args.t)
	v= float(args.v)
	g= 9.81
	y= v*t-.5*g*t**2
	print y
except:
	print "invalid input try again"