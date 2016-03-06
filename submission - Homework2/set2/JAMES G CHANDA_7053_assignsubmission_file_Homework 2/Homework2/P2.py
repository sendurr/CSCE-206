#P2: wrtie a program that prints a table with t values in the first column and
#corresponding y(t) = v0t - 0.5gt^2 values in the second column.
#Use n uniformly spaced t values throughout the interval [0, 2v0/g].
#Set v0= 1, g= 9.81, and n = 11. 

from math import *

def y(t,v0,g):
	answer = (v0*t)-(0.5((g*(t**2.0))))
	return answer

v = 5.0 #Initial velocity of the ball
g = 9.81 #gravity
t= 0.0 #time
interval = 2.0*(v/g)
i = 0
tvalues = interval/11 #step size

print "t\t\t\ty(t)"
while t < interval:
	y = (v*t)- (0.5 *g*t**2)
	print "%f\t%f" %(t,y)
	t+= tvalues




