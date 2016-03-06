import argparse

g = 9.81

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v0', help='initial velocity')
parser.add_argument('-t', action='store', dest='t', help='time')                            
try:
	args = parser.parse_args()
	y = float(args.v0)*float(args.t) - 0.5*g*float(args.t)**2
	print y

except:
	v0 = float(raw_input("Input velocity: "))
	t = float(raw_input("Input time: "))
	y = v0*t - 0.5*g*t**2
	print y

