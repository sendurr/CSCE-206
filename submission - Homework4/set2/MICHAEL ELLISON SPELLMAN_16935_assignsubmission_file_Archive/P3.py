from matplotlib.pylab import *
import sys

g=9.81
n=51
curves=3
v0=zeros(curves)

if len(sys.argv)<4:
	print "Usage: python %s v0_1 v0_2 v0_3"%sys.argv[0]
	sys.exit(1)

#User input 
for i in range(curves):
	v0[i]=float(sys.argv[i+1])

t=zeros((curves,n))
y=zeros((curves,n))
for x in xrange(curves):
	t[x]=linspace(0,2*v0[x]/g,n)
	y[x]=v0[x]*t[x]-0.5*g*t[x]**2


for i in range(curves):
	l='v0='+str(v0[i]) 
	plot(t[i],y[i],label=l)
	hold('True')

legend()
xlabel('time')
ylabel('y(t)')
title('Homework 4 - P3')
show()