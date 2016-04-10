from matplotlib.pylab import *
import sys

g=9.81
n=51
data_sets=3
v0=zeros(data_sets)

for i in range(data_sets):
	v0[i]=float(sys.argv[i+1])

t=zeros((data_sets,n))
y=zeros((data_sets,n))
for x in xrange(data_sets):
	t[x]=linspace(0,2*v0[x]/g,n)
	y[x]=v0[x]*t[x]-0.5*g*t[x]**2

for i in range(data_sets):
	l='v0='+str(v0[i]) 
	plot(t[i],y[i],label=l)
	hold('True')

legend()
xlabel('time')
ylabel('y(t)')
title('Problem 3')
show()