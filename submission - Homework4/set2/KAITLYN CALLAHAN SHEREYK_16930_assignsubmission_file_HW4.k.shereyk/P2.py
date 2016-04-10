# Kate Shereyk
import numpy as numpy
import matplotlib.pyplot as plt
import sys
from math import *
from pylab import *
x=arange(-3.14,3.14,0.01)
y=(exp(x**2))*sin(x)
plot(x,y)
grid(True)
title('Plot figure for function')
show()