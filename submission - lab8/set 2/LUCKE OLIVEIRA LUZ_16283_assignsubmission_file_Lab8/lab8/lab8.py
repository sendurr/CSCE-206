# Name: Lucke Oliveira Luz			Assignment: Lab 8

import numpy as np
import matplotlib.pylab as plt

air = open("density_air.dat",'r')
water = open("density_water.dat",'r')

air_data = air.readlines()
water_data = water.readlines()

air_temp = []
air_density = []
water_temp = []
water_density = []

for line in air_data:
	if "#" in line or line == "\n":
		continue
	else:
		values = line.strip().split()
		air_temp.append(float(values[0]))
		air_density.append(float(values[1]))

air_1deg = np.polyfit(air_temp,air_density,1)
air_2deg = np.polyfit(air_temp,air_density,2)
a1 = np.poly1d(air_1deg)
a2 = np.poly1d(air_2deg)
a1 = a1(air_temp)
a2 = a2(air_temp)

plt.plot(air_temp,air_density,'bo',air_temp,a1,'r--',air_temp,a2,'k--')
plt.legend(['data','fitted degree 1 polynomial','fitted degree 2 polynomial'])
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Air Density (kg/m^3)')
plt.title('Temperature dependence of air density')
plt.axis([-15.0,35.0,1.15,1.37])
plt.figure()

for line in water_data:
	if "#" in line or line == "\n":
		continue
	else:
		values = line.strip().split()
		water_temp.append(float(values[0]))
		water_density.append(float(values[1]))

water_1deg = np.polyfit(water_temp,water_density,1)
water_2deg = np.polyfit(water_temp,water_density,2)
w1 = np.poly1d(water_1deg)
w2 = np.poly1d(water_2deg)
w1 = w1(water_temp)
w2 = w2(water_temp)

plt.plot(water_temp,water_density,'bo',water_temp,w1,'r--',water_temp,w2,'k--')
plt.legend(['data','fitted degree 1 polynomial','fitted degree 2 polynomial'])
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Water Density (kg/m^3)')
plt.title('Temperature dependence of water density')
plt.axis([-5.0,105.0,955.0,1008.0])
plt.show()
