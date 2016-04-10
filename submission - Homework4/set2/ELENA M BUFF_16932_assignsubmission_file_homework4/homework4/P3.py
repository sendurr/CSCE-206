from matplotlib.pylab import *
import sys

g=9.81
n=51
nocurves=3
v0=zeros(nocurves)



for i in range(nocurves):
	v0[i]=float(sys.argv[i+1])

t=zeros((nocurves,n))
y=zeros((nocurves,n))
for x in xrange(nocurves):
	t[x]=linspace(0,2*v0[x]/g,n)
	y[x]=v0[x]*t[x]-0.5*g*t[x]**2



for i in range(nocurves):
	l='v0='+str(v0[i]) 
	plot(t[i],y[i],label=l)
	hold('True')

legend()
xlabel('time (s)')
ylabel('position (m)')
title('Homework Problem 3')
show()