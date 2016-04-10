# Jeremy Abrams
# CSCE 206
# Lab 8 - fit_density_data.py
# March 20, 2016


from matplotlib.pyplot import *
from math import *
from numpy import *
import sys

water_temp = []
water_density = []
air_temp = []
air_density = []

water_file = open("density_water.dat", 'r')
air_file = open("density_air.dat", 'r')

water_data = water_file.readlines()
air_data = air_file.readlines()

for data in water_data:
	data.strip("\n")
	if(data[0][0] != "#"):
		if(data[0][0] != "\n"):
			temp_data = data.strip().split("   ")
			water_temp.append(temp_data[0])
			water_density.append(temp_data[1])

for data in air_data:
	data.strip("\n")
	if(data[0][0] != "#"):
		if(data[0][0] != "\n"):
			temp_data = data.strip().split("   ")
			air_temp.append(temp_data[0])
			air_density.append(temp_data[1])

air_array = array([air_temp, air_density], dtype=float)
water_array = array([water_temp, water_density], dtype=float)
air_coeff_d1 = polyfit(air_array[0], air_array[1], 1)
water_coeff_d1 = polyfit(water_array[0], water_array[1], 1)
air_coeff_d2 = polyfit(air_array[0], air_array[1], 2)
water_coeff_d2 = polyfit(water_array[0], water_array[1], 2)
air_p_d1 = poly1d(air_coeff_d1)
water_p_d1 = poly1d(water_coeff_d1)
air_p_d2 = poly1d(air_coeff_d2)
water_p_d2 = poly1d(water_coeff_d2)

air_density_fit_d1 = air_p_d1(air_array[0])
water_density_fit_d1 = water_p_d1(water_array[0])

air_density_fit_d2 = air_p_d2(air_array[0])
water_density_fit_d2 = water_p_d2(water_array[0])

plot(air_array[0], air_array[1], 'bo', label='Data')
plot(air_array[0], air_density_fit_d1, 'r--', label='fitted degree 1 polynomial')
plot(air_array[0], air_density_fit_d2, 'g--', label='fitted degree 2 polynomial')
xlabel('Temperature')
ylabel('Density')
legend()
figure
title("Temperature dependence of air density")
show()

plot(water_array[0], water_array[1], 'bo', label='Data')
plot(water_array[0], water_density_fit_d1, 'r--', label='fitted degree 1 polynomial')
plot(water_array[0], water_density_fit_d2, 'g--', label='fitted degree 2 polynomial')
xlabel('Temperature')
ylabel('Density')
legend()
title("Temperature dependence of air density")
show()
