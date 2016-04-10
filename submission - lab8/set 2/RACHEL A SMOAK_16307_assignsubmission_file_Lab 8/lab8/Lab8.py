#Rachel Smoak
#20 March 2016
#Lab 8

import operator
import numpy as np
import matplotlib.pyplot as plt

Water_temp = []
water_density = []
Air_temp = []
air_density = []

infile1=open('density_water.dat', 'r' )
lines1 = infile1.readlines()
for x in lines1:
	if x== '\n' or x[0]=="#":
		continue
	items1 = x.strip().split("   ")
	Water_temp.append(float(items1[0]))
	water_density.append(float(items1[1]))

infile2=open('density_air.dat', 'r' )
lines2 = infile2.readlines()
for x in lines2:
	if x== '\n' or x[0]=="#":
		continue
	items2 = x.strip().split("   ")
	Air_temp.append(float(items2[0]))
	air_density.append(float(items2[1]))

coeff1a = np.polyfit(Water_temp, water_density,1)
coeff1b = np.polyfit(Water_temp, water_density,2)
poly1a = np.poly1d(coeff1a)
poly1b = np.poly1d(coeff1b)
coeff2a = np.polyfit(Air_temp, air_density,1)
coeff2b = np.polyfit(Air_temp, air_density,2)
poly2a = np.poly1d(coeff2a)
poly2b = np.poly1d(coeff2b) 

water_density_fit1 = []
air_density_fit1 = []
water_density_fit2 = []
air_density_fit2 = []

for i in Water_temp:
	a = poly1a(i)
	b = poly1b(i)
	water_density_fit1.append(a)
	water_density_fit2.append(b)
for i in Air_temp:
	a = poly2a(i)
	b = poly2b(i)
	air_density_fit1.append(a)
	air_density_fit2.append(b)

plt.figure(1)
plt.subplot(122)
plt.plot(Water_temp, water_density, marker = 'o', linestyle = '')
plt.plot(Water_temp,water_density_fit1, linestyle = "--")
plt.plot(Water_temp,water_density_fit2, linestyle = '--')
plt.legend(['Data', 'Fitted degree 1 polynomial', 'Fitted degree 2 polynomial'])
plt.title('Temperature Dependence of Water Density')
plt.xlabel('Temperature (C)')
plt.ylabel('Density (kg/m^3)')
axes = plt.gca()
axes.set_xlim([-5,105])
plt.subplot(121)
plt.plot(Air_temp,air_density, marker = 'o', linestyle = '')
plt.plot(Air_temp, air_density_fit1, linestyle = '--')
plt.plot(Air_temp, air_density_fit2, linestyle = '--')
plt.legend(['Data', 'Fitted degree 1 polynomial', 'Fitted degree 2 polynomial'])
plt.title('Temperature Dependence of Air Density')
plt.xlabel('Temperature (C)')
plt.ylabel('Density (kg/m^3)')
axes = plt.gca()
axes.set_xlim([-15,35])
plt.show()