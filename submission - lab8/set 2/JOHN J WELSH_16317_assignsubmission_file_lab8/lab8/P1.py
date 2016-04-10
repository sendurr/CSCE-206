from numpy import *
from matplotlib.pylab import *

water_file = open('density_water.dat', 'r')
air_file = open('density_air.dat', 'r')

water_lines = water_file.readlines()
air_lines = air_file.readlines()

Water_temp = []; water_density = []; Air_temp = []; air_density = []
for line in water_lines:
	if line == '\n' or line[0] == '#':
		continue
	data = line.split()
	Water_temp.append(float(data[0]))
	water_density.append(float(data[1]))

for line in air_lines:
	if line == '\n' or line[0] == '#':
		continue
	data = line.split()
	Air_temp.append(float(data[0]))
	air_density.append(float(data[1]))

coeff = polyfit(Water_temp, water_density, 1)
p = poly1d(coeff)
y_water_deg1 = p(Water_temp)
coeff = polyfit(Water_temp, water_density, 2)
p = poly1d(coeff)
y_water_deg2 = p(Water_temp)
coeff = polyfit(Air_temp, air_density, 1)
p = poly1d(coeff)
y_air_deg1 = p(Air_temp)
coeff = polyfit(Air_temp, air_density, 2)
p = poly1d(coeff)
y_air_deg2 = p(Air_temp)

figure(1)
subplot(121)
plot(Air_temp,air_density, 'o', Air_temp, y_air_deg1, 'b--', Air_temp, y_air_deg2, 'r--')
legend(['data', 'fitted degree 1 polynomial', 'fitted degree 2 polynomial'])
title('Temperature dependence of air desnity')
xlabel('Temperature')
ylabel('Density')
axis([-15, 35, 1.15, 1.375])
subplot(122)
plot(Water_temp,water_density, 'o', Water_temp, y_water_deg1, 'b--', Water_temp, y_water_deg2, 'r--')
legend(['data', 'fitted degree 1 polynomial', 'fitted degree 2 polynomial'])
title('Temperature dependence of water desnity')
xlabel('Temperature')
ylabel('Density')
axis([-10, 110, 955, 1005])
show()

water_file.close()
air_file.close()