from numpy import *
import sys
import matplotlib.pylab as plt
 
if len(sys.argv)>=5 or len(sys.argv)<=3:
    print ("Enter exactly three v_0 parameters")
    sys.exit()


g=9.81
v_0= float(sys.argv[1])
v_1= float(sys.argv[2])
v_2= float(sys.argv[3])

def f1(t0):
    return (v_0*t0)-(0.5*g*t0**2)

t0 = linspace(0, 2*v_0/g, 100)
fv1 = vectorize(f1)
y1 = fv1(t0)

def f2(t1):
    return (v_1*t1)-(0.5*g*t1**2)

t1 = linspace(0, 2*v_1/g, 100)
fv2 = vectorize(f2)
y2 = fv2(t1)

def f3(t2):
    return (v_2*t2)-(0.5*g*t2**2)

t2 = linspace(0, 2*v_2/g, 100)
fv3 = vectorize(f3)
y3 = fv3(t2)

for i in xrange(len(t0)):
    y1[i] = f1(t0[i])
plt.plot(t0,y1,'yo')
plt.hold(True)

for i in xrange(len(t1)):
    y2[i] = f2(t1[i])
plt.plot(t1,y2,'r')
plt.hold(True)

for i in xrange(len(t2)):
    y3[i] = f3(t2[i])
plt.plot(t2,y3,'g')

plt.show()
