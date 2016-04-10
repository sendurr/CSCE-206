import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81


def y(t, v0):
    return v0 * t - 0.5 * g * t ** 2

x = plt.subplot(111)
plt.hold(1)


def curve(v0):
    tlist = np.linspace(0, 2 * v0 / g, 100)
    x.plot(tlist, y(tlist, v0))

x.set_xlabel('time (s)')
x.set_ylabel('height (m)')

vector = np.array(sys.argv[1:], dtype=np.float)

for i in range(len(vector)):
    curve(vector[i])
plt.legend(['v0 = %g' % v0 for v0 in vector])
plt.show()