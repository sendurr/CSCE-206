from math import sin, exp
from numpy import *
from matplotlib.pylab import *
import sys

#requires 3 inputs

v1=float(sys.argv[1])
v2=float(sys.argv[2])
v3=float(sys.argv[3])

g=float(9.81)

def time(y):
	a=(2*y)/g
	return a
def position(v,t):
	b=v*t-(.5*(g*t**2))
	return b
def tline(z):
	c=linspace(0,time(z),101)
	return c

most=max(v1,v2,v3)
y_lim=max((position(most,tline(most)))*1.1)

plot(tline(v1), position(v1,tline(v1)),'r--', label=v1)
plot(tline(v2), position(v2,tline(v2)),'b--', label=v2)
plot(tline(v3), position(v3,tline(v3)),'g--', label=v3)
legend(loc='upper right')
ylim([0,y_lim])
xlim(0)
grid(True)
xlabel('Time (seconds)')
ylabel('Position (Meters)')
title('Relative Position of Projectile')
show()
