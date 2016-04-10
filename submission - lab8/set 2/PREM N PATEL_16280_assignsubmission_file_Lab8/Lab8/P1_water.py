import numpy as np
from matplotlib.pylab import *

data = np.loadtxt("density_water.dat", dtype=np.float)

water_temp = data[:,0]
water_density = data[:,1]

coeff1 = np.polyfit(water_temp, water_density, 1)
p1 = np.poly1d(coeff1)
print p1
water_density_fit1 = p1(water_temp)

coeff2 = np.polyfit(water_temp, water_density, 2)
p2 = np.poly1d(coeff2)
print p2
water_density_fit2 = p2(water_temp)

waterplot0 = plot(water_temp, water_density, 'bo', label='data')
waterplot1 = plot(water_temp, water_density_fit1, 'r--', label='fitted polynomial of deg 1')
waterplot2 = plot(water_temp, water_density_fit2, 'b--', label='fitted polynomial of deg 2')
xlabel('temperature')
ylabel('density')
title('Temperature Dependence of Water Density')
legend()
show()