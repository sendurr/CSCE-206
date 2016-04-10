# Name: Lucke Oliveira Luz			Assignment: Homework 4        Exercise: 3

from matplotlib.pylab import *
from numpy import *
import sys

def y(v0,t): 
	g = 9.81
	y = v0*t - 0.5*g*t**2
	return y

def t(v0):
	g = 9.81
	t = arange(0.0,2*v0/g+0.01,0.01)
	return t

v01 = float(sys.argv[1])
v02 = float(sys.argv[2])
v03 = float(sys.argv[3])

plot(t(v01),y(v01,t(v01)))
hold('on')
plot(t(v02),y(v02,t(v02)))
hold('on')
plot(t(v03),y(v03,t(v03)))
hold('on')
xlabel('t')
ylabel('y(t)')
legend(['v0 = %.1f'%(v01),'v0 = %.1f'%(v02),'v0 = %.1f'%(v03)])
show()