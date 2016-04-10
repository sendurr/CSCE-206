import matplotlib.pyplot as plt 
from math import sin
from numpy import *
xlist=[]
ylist=[]
x0=-3.14
x1=3.14
step= (x1-x0)/99.0
for i in range(100):
	x=x0+i*step
	#print (x)
	y=exp(x**2)*sin(x)
	xlist.append(x)
	ylist.append(y)
plt.plot (xlist,ylist)
plt.show()
