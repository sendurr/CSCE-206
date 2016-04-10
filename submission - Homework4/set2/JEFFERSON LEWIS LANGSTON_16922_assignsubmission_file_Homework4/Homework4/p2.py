from numpy import *
from matplotlib.pylab import *
import sys

def f(x):
    return exp(x**2)*sin(x)

x = linspace(-3.14, 3.14, 50)
y = zeros(len(x), 'd')

for j in xrange(len(x)):
    y[j] = f(x[j])

plot(x, y)
show()
