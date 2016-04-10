
import numpy as np
import matplotlib.pyplot as plt


def f(n):
	return np.exp(n**2)*np.sin(n)

n=([-3.14, 3.14])

xlist=[]
ylist=[]
for x in n:
	print n
	y=f(x)
	xlist.append(x)
	ylist.append(y)

print xlist,ylist

plt.plot(xlist,ylist)
plt.title("curve")
plt.show()