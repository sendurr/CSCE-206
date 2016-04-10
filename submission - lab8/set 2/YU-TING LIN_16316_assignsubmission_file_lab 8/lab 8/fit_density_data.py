import numpy as np
import matplotlib.pyplot as plt
import sys

myarray = np.fromfile('density_water.dat',dtype=float)

Water_temp=[]
water_density=[]

coeff=polyfit(x,y,deg)
P=poly1d(coeff)
print p
y-fitted=p(x)
plot(x,y,'r-',x,y+fitted,'b-',
	legend=('data','fitted polynomial of degree %d' % deg))
Axis([0, 100, 958, 1000])
Title('Temperature dependence of water density')


plt.show()