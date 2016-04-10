from numpy import *
from matplotlib.pylab import *
import sys

v1=float(sys.argv[1])
v2=float(sys.argv[2])
v3=float(sys.argv[3])

g=9.81

X1=linspace(0, (2*v1/g),50)
X2=linspace(0, (2*v2/g),50)
X3=linspace(0, (2*v3/g),50)

Y1=(v1*X1 - 0.5*g*X1**2)
Y2=(v2*X2 - 0.5*g*X2**2)
Y3=(v3*X3 - 0.5*g*X3**2)

plt.figure('P3.py Figure')

plt.hold(True)

plt.plot(X1,Y1)
plt.plot(X2,Y2,'r*')
plt.plot(X3,Y3,'bo')

plt.show()