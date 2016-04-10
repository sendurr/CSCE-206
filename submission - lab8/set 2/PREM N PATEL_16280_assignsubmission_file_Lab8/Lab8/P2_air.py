import numpy as np
from matplotlib.pylab import *

data = np.loadtxt("density_air.dat", dtype=np.float)

air_temp = data[:,0]
air_density = data[:,1]

coeff1 = np.polyfit(air_temp, air_density, 1)
p1 = np.poly1d(coeff1)
print p1
air_density_fit1 = p1(air_temp)

coeff2 = np.polyfit(air_temp, air_density, 2)
p2 = np.poly1d(coeff2)
print p2
air_density_fit2 = p2(air_temp)

airplot0 = plot(air_temp, air_density, 'bo', label='data')
airplot1 = plot(air_temp, air_density_fit1, 'r--', label='fitted polynomial of deg 1')
airplot2 = plot(air_temp, air_density_fit2, 'b--', label='fitted polynomial of deg 2')
xlabel('temperature')
ylabel('density')
title('Temperature Dependence of Air Density')
legend()
show()