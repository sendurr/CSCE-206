from numpy import *
from matplotlib.pylab import *

air = open('density_air.dat', 'r')
airLines = air.readlines()
#opens and reads air file
Air_temp = []
air_density = []
#initializes temp and density arrays
for line in airLines:
	if line[0] == '#' or line == '\n':
		continue
		#starts at the right locations and then ignores the non-number characters
	num = line.split()
	Air_temp.append(float(num[0]))
	air_density.append(float(num[1]))
	#adds the split data to the arrays

water = open('density_water.dat', 'r')
waterLines = water.readlines()
#opens and reads water file
Water_temp = []
water_density = []
#initializes temp and density arrays
for line in waterLines:
	if line[0] == '#' or line == '\n':
		continue
		#starts at the right locations and then ignores the non-number characters
	num = line.split()
	Water_temp.append(float(num[0]))
	water_density.append(float(num[1]))
	#adds the split data to the arrays

coeff = polyfit(Air_temp, air_density, 1)
p = poly1d(coeff)
y_air1 = p(Air_temp)

coeff = polyfit(Air_temp, air_density, 2)
p = poly1d(coeff)
y_air2 = p(Air_temp)

coeff = polyfit(Water_temp, water_density, 1)
p = poly1d(coeff)
y_water1 = p(Water_temp)

coeff = polyfit(Water_temp, water_density, 2)
p = poly1d(coeff)
y_water2 = p(Water_temp)
#fits the polynomials to the data as shown in the lab instructions

figure(1)
subplot(121)

plot(Air_temp,air_density, 'o', Air_temp, y_air1, 'b--', Air_temp, y_air2, 'r--')

legend(['Data', 'Fitted Degree 1 Polynomial', 'Fitted Degree 2 Polynomial'])
title('Temperature Dependence of Air Density')
xlabel('Temperature')
ylabel('Density')

axis([-15, 35, 1.15, 1.375])
subplot(122)

plot(Water_temp, water_density, 'o', Water_temp, y_water1, 'b--', Water_temp, y_water2, 'r--')

legend=('Data', 'Fitted Degree 1 Polynomial', 'Fitted Degree 2 Polynomial')
title('Temperature Dependence of Water Density')
xlabel('Temperature')
ylabel('Density')

axis([-10, 110, 955, 1005])

show()

water.close()
air.close()