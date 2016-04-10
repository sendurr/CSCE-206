from numpy import *
from matplotlib.pylab import *

t = linspace(-3.14, 3.14, 100)

f = []
for x in t:
	f.append(math.exp(x**2)*math.sin(x))

plot(t,f)
show()