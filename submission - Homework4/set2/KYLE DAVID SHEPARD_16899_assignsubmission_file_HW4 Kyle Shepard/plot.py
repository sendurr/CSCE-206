from math import sin, exp
from numpy import *
from matplotlib.pylab import *


def f(x):
    a=exp(x**2)*sin(x)
    return a

t=linspace(-3.14,3.14,501)

plot(t,f(t), 'r', label="e^(x^2)*sin(x)")
grid(True)
legend(loc='upper center')
xlim([-3.14,3.14])
show()