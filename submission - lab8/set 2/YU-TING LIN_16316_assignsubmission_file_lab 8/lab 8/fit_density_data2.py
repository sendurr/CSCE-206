import numpy as np
import matplotlib.pyplot as plt
import sys

myarray = np.fromfile('density_air.dat',dtype=float)
Air_temp=[]
air_density=[]

coeff=polyfit(x,y,deg)
P=poly1d(coeff)
print p
y-fitted=p(x)
plot(x,y,'r-',x,y+fitted,'b-',
	legend=('data','fitted polynomial of degree %d' % deg))
Axis([-10, 30, 1, 1.4])
Title('Temperature dependence of air density')


plt.show()