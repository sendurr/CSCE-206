from numpy import *
from matplotlib.pylab import *

t = linspace(-3.14, 3.14, 100)

F = []
for x in t:
	F.append(math.exp(x**2)*math.sin(x))

plot(t,F)
show()