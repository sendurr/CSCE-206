from matplotlib.pylab import *
import sys
g = 9.81
n = 51
data = 3
v0 = zeros(data)

for i in range(data):
    v0[i] = float(sys.argv[i+1])

t = zeros((data,n))
y = zeros((data,n))
for x in xrange(data):
    t[x] = linspace(0,2*v0[x]/g,n)
    y[x] = v0[x]*t[x]-0.5*g*t[x]**2

for i in range(data):
    label = 'v0='+str(v0[i])
    plot(t[i],y[i],label=label)

legend()
xlabel('t')
title('P3')
ylabel('y(t)')
show()