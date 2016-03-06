import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-v0', action='store', dest='v0',default=0, help='value for v0:')
parser.add_argument('-t', action='store', dest='t',default=0, help='value for t:')

args=parser.parse_args()

try:
	v0=float(args.v0)
except:
	print "ERROR v0 is not a number"
	v0 = eval(raw_input("v0 = ?\n"))

try:
	t=float(args.t)
except: 
	print "ERROR t is not a number"
	t = eval(raw_input("t = ?\n"))

g = 9.81

y = v0*t - 0.5*g*t**2

print y
