import sys
from matplotlib.pyplot import *
from numpy import *

v= sys.argv[1]
v=float(v)
g= 9.81
t= np.linspace(0, (2*v)/g, 100)
y= np.array((v*t)-(.5*g*t**2))

b= sys.argv[2]
b=float(b)
e=np.linspace(0, (2*b)/g, 100)
f=np.array(b*e-.5*g*e**2)

r= sys.argv[3]
r=float(r)
s= np.linspace(0, (2*r)/g, 100)
g=np.array(r*s-.5*g*s**2)

plot(t,y,'r-',e,f,'b-',s,g,'g-')
show(plot)