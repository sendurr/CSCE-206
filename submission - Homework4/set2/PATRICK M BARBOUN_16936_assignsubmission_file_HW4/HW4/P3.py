import sys as sys
import numpy as np 
import matplotlib.pyplot as py 

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
g = 9.8

t1 = 2*a/g
t2 = 2*b/g
t3 = 2*c/g

doma = np.arange(0,t1,0.1)
domb = np.arange(0,t2,0.1)
domc = np.arange(0,t3,0.1)

y1 = a*doma-0.5*g*doma**2
y2 = b*domb-0.5*g*domb**2
y3 = c*domc-0.5*g*domc**2

py.xlabel("Time (s)")
py.ylabel("Vertical Distance (m)")
py.plot(doma,y1,"bo")
py.plot(domb,y2,"rh")
py.plot(domc,y3,"gd")
py.show()

