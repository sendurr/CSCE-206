import sys
import matplotlib.pylab as plt 
from numpy import *

def f(x):
    return exp(x**2)*sin(x)

x = linspace(-3.14, 3.14, 100)
fv=vectorize(f)
y=fv(x)

plt.plot(x, y)
plt.show()
