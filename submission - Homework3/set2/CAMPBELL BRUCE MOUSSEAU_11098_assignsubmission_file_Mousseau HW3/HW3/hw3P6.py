import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v0','--v0', type=float)
parser.add_argument('-t','--t', type=float)

args = parser.parse_args()
g = 9.81

try:
	v0 = float(args.v0)
	t = float(args.t)
except:
	print 'Error, input again using the raw_input function.'
	v0 = float(raw_input('Please enter v0:'))
	t = float(raw_input('Please enter t:'))
y = (v0*t)-(0.5*g*t**2)
print (y)
