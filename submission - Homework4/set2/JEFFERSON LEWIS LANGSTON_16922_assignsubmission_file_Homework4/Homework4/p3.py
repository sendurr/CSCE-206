import sys
from numpy import *
from matplotlib.pylab import *
 
if len(sys.argv) <=3 or len(sys.argv)>=5:
    print "Enter exctly three v0 parameters"
    sys.exit()

g = 9.81
v01 = float(sys.argv[1])
v02 = float(sys.argv[2])
v03 = float(sys.argv[3])

def f1(t1):
    return (v01*t1)-(0.5*g*t1**2)

t1 = linspace(0, 2*v01/g, 50)
y1 = zeros(len(t1), 'd')

def f2(t2):
    return (v02*t2) - (0.5*g*t2**2)

t2 = linspace(0, 2*v02/g, 50)
y2 = zeros(len(t2), 'd')

def f3(t3):
    return (v03*t3)-(0.5*g*t3**2)

t3 = linspace(0, 2*v03/g, 50)
y3 = zeros(len(t3), 'd')

for i in xrange(len(t1)):
    y1[i] = f1(t1[i])
plot(t1,y1,'yo')
hold

for i in xrange(len(t2)):
    y2[i] = f2(t2[i])
plot(t2,y2,'r')
hold

for i in xrange(len(t3)):
    y3[i] = f3(t3[i])
plot(t3,y3,'g')

show()
