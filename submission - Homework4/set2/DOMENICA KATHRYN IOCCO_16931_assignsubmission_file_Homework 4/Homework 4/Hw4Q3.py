from numpy import *
from matplotlib.pylab import *
import sys
import argparse
g=9.81
v0=np.arange(1.0, 2.2, 5.0)
#v0=eval(sys.argv[3])
t=linspace(0,2*v0/g)
def f(t):
		y=(v0*t)-(0.5*g*t**2)
		return y
f1=np.vectorize(f)
y1=f1(t)
print(y1)
plt.plot(t, y1, 'r--', t**2, y1, 'b--', t**3, y1, 'g--')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Three Values on One Graph')
plt.legend(['V0=1.0', 'V0=2.2', 'V0=5.0'])
plt.show()