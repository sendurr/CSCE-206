from matplotlib.pylab import *
import sys


x = linspace(-3.14, 3.14)
y = exp(x**2)*sin(x)
plot(x, y)

xlabel('x')
ylabel('y')
legend('exp(x^2)*sin(x)')
title('Homework Problem 2')
show()
sys.exit(1)