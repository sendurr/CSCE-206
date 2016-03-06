import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v',default=0, help='v')
parser.add_argument('-t', action='store', dest='t',default=0, help='t')
args = parser.parse_args()

v=eval(args.v)
t=eval(args.t)

g=9.81
y = v0*t - 0.5*g*t**2
print (v,t)

print (y) 
	
