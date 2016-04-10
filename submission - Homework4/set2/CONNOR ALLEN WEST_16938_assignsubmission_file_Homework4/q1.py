
# Q3
import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81


def y(t, v0):
    return v0 * t - 0.5 * g * t ** 2

x = plt.subplot()
plt.hold()


def plot_trajectory(v0):
    time_list = np.linspace(0, 2 * v0 / g, 100)
    x.plot(time_list, y(time_list, v0))


speeds = np.array(sys.argv[1:], dtype=np.float)

for x in speeds:
    plot_trajectory(x)

plt.show()

