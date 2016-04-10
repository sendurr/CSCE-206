import numpy as np
import matplotlib.pylab as plt

data_water = open('density_water.dat', 'r')
data_air = open('density_air.dat', 'r')
Water_temp = []; water_density = []; Air_temp = []; air_density = []
lines_w = data_water.readlines()
lines_a = data_air.readlines()

for line in lines_a:
	if line == '\n' or line[0] == '#':
		continue
	numbers = line.split()
	Air_temp.append(float(numbers[0]))
	air_density.append(float(numbers[1]))

for line in lines_w:
	if line == '\n' or line[0] == '#':
		continue
	numbers = line.split()
	Water_temp.append(float(numbers[0]))
	water_density.append(float(numbers[1]))
	

coefficients = np.polyfit(Water_temp, water_density, 1); equation = np.poly1d(coefficients); water_fitted_1 = equation(Water_temp)
coefficients = np.polyfit(Water_temp, water_density, 2); equation = np.poly1d(coefficients); water_fitted_2 = equation(Water_temp)
coefficients = np.polyfit(Air_temp, air_density, 1); equation = np.poly1d(coefficients); air_fitted_1 = equation(Air_temp)
coefficients = np.polyfit(Air_temp, air_density, 2); equation = np.poly1d(coefficients); air_fitted_2 = equation(Air_temp)

plt.figure(1)
plt.subplot(211)
plt.plot(Air_temp,air_density, 'o', Air_temp, air_fitted_1, 'b--', Air_temp, air_fitted_2, 'r--')
plt.axis([-16, 34, 1.12, 1.4])
plt.legend(['data', 'fitted degree 1 polynomial', 'fitted degree 2 polynomial'])
plt.title('Temperature dependence of air desnity')
plt.xlabel('Temperature')
plt.ylabel('Density')
plt.subplot(212)
plt.plot(Water_temp,water_density, 'o', Water_temp, water_fitted_1, 'b--', Water_temp, water_fitted_2, 'r--')
plt.axis([-10, 110, 955, 1005])
plt.legend=('data', 'fitted degree 1 polynomial', 'fitted degree 2 polynomial')
plt.title('Temperature dependence of water desnity')
plt.xlabel('Temperature')
plt.ylabel('Density')
plt.show()
data_water.close()
data_air.close()