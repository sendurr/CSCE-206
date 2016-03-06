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

v0= float(args.velocity)
t= float(args.time)

print (y(v0,t,g))