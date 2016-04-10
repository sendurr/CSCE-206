from numpy import *
from matplotlib.pylab import *
import sys

g=9.81
def y(v0,t,g):
	y=v0*t-0.5*g*t**2
	return y

v1=float(sys.argv[1])
v2=float(sys.argv[2])
v3=float(sys.argv[3])

t1=linspace(0,(2.0*v1)/g,100)
t2=linspace(0,(2.0*v2)/g,100)
t3=linspace(0,(2.0*v3)/g,100)

plot(t1,y(v1,t1,g),'r*')
hold('on')
plot(t2,y(v2,t2,g),'bo')
hold('on')
plot(t3,y(v3,t3,g),'g-')

show()