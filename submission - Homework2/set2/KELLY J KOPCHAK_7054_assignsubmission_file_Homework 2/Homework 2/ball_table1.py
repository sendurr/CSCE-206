from math import *
v0=1
g=9.81
n=11
t=0
stepsize=(2*v0/g)/n
while t<=((2*v0/g)+0.01853):
	y=(1*t)-(0.5*9.81*(t**2))
	print "%5.5f %5.5f"% (t,y)
	t+=stepsize

print 2*v0/g