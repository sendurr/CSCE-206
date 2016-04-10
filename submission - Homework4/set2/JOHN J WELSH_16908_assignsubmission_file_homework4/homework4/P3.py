from sys import argv
import matplotlib.pyplot as plt
import numpy as np 
g = 9.81 

for i in range(1,4):
	y0 = []
	v = float(argv[i])
	t = np.linspace(0, 2*v/g, 100)
	for e in t:
		y0.append(v*e-0.5*g*e**2)
	label = "v0 = " + str(v)
	plt.plot(t, y0, label = label)

plt.legend()
plt.xlabel('t'); plt.ylabel('y(t)')
plt.show()