from numpy import *
e=linspace( -3.14, 3.14, 100)
def f(x):
	p= exp(x**2)* sin(x)
	return p

y=[]
for i in e:
	y.append(f(i))
plot(e,y,'r*')
show(plot)