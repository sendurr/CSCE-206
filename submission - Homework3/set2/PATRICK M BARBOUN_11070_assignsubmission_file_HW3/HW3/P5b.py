import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', action = 'store', dest = 'v', default = '5', help = 'initial velocity')
parser.add_argument('-t', action = 'store', dest = 't', default = '0.8', help = 'time elapsed')
args = parser.parse_args()

try:
	v = eval(args.v)
	t = eval(args.t)

except NameError:
	print 'Error: input must be a number'
	v = float(raw_input('initial velocity'))
	t = float(raw_input('elapsed time'))

print v*t-0.5*9.8*t**2
