from numpy import *
from matplotlib.pylab import *

def F(x):
	return exp(x**2)*sin(x)

x=linspace(-3.14,3.14,100)

plt.plot(x,F(x),'-')
plt.show()