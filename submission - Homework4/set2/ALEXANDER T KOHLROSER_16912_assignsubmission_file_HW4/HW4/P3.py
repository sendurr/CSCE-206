from sys import argv
import matplotlib.pyplot as plt
import numpy as np 

g = 9.81 

for i in range(1,4):
	y = []
	v = float(argv[i])
	t = np.linspace(0, 2*v/g, 100)
	
	for x in t:
		y.append(v * x - 0.5 * g * x**2)
	
	label = "v0 = " + str(v)
	plt.plot(t, y, label = label)

plt.legend()

plt.xlabel('t'); plt.ylabel('y(t)')

plt.show()