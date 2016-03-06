import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-v0', action='store', dest='velocity',default=1, help='velocity')
parser.add_argument('-t', action='store', dest='time',default=1, help='time')                            
args = parser.parse_args()

print (args.velocity)
print (args.time)

g=9.81
def y(v0,t,g):
	y=v0*t-0.5*g*t**2
	print (y)

try:
	v0=float(args.velocity)
except:
	print ("Error: input not a number")
	v0=raw_input("v0=")
	v0=float(v0)

try:
	t=float(args.time)
except:
	print ("Error: input not a number")
	t=raw_input("t=")
	t=float(t)

print (y(v0,t,g))