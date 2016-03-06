import sys

g=9.81
def y(v0,t,g):
	y=v0*t-0.5*g*t**2
	print (y)

print (sys.argv)

v0=float(sys.argv[1])
t=float(sys.argv[2])

print (y(v0,t,g))