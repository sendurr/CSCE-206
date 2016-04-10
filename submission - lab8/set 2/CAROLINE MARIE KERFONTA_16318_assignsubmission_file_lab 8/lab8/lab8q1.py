from numpy import *
import matplotlib.pyplot as plt 

xlist=[]
ylist=[]
x0=0
x1=30
step= (x1-x0)/9
for i in range(30):
	x=x0+i*step
	print (x)
	y=1.35-15*x 
	xlist.append(x)
	ylist.append(y)
print (xlist,ylist)
plt.title("Temperature dependence of air density")
plt.show()

x0=0
x1=100
step= (x1-x0)/8
for i in range(100):
	x=x0+i*step
	print (x)
	y=x^2
	xlist.append(x)
	ylist.append(y)
print (xlist,ylist)
plt.title("Temperature of dependence of water density")
plt.show()

coeff = polyfit(x, y, deg)
p = poly1d(coeff)
print (p)
y_fitted = p(x)
plot(x, y, '-r', x, y_fitted, '-b')
lengend=('data', 'density of air to temperature')

coeff = polyfit(x, y, deg)
t = poly1d(coeff)
print (t)
y_fitted = p(x)
plot(x, y, '-r', x, y_fitted, '-b')
lengend=('data', 'density of water to temperature')

