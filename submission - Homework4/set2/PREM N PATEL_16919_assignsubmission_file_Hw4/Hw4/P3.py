import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81

for i in range(1, len(sys.argv)):
	v = float(sys.argv[i])
	t = np.linspace(0, 2*v/g, 100)
	y = v*t - 0.5*g*t**2
	plt.plot(t,y)

plt.show()