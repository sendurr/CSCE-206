from matplotlib.pylab import *
import sys

def f(x):
	return exp(x**2)*sin(x)

t = linspace(-3.14,3.14,51)
y = zeros(len(t), 'd') 
for i in xrange(len(t)):
	y[i]=f(t[i])
print t
print y

plot(t, y)

xlabel('x') 
ylabel('y')
legend('exp(x^2)*sin(x)')
title('Hw 4:Problem2')
show()