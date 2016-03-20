'''################################################################################
    CSCE 206 Lab8  , Exercise Q1
    Fit a polynomial to data and plot a graph
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from numpy import *
from matplotlib.pyplot import *

water_temp = []
water_density = []
air_temp = []
air_density = []

input_file=open("density_water.dat",'r')
lines=input_file.readlines()

for x in lines:
	if x[0]=="#" or x[0]=="\n":
		continue
	else:
		data = x.strip().split("   ")
		water_temp.append(float(data[0]))
		water_density.append(float(data[1]))

print ("Printing the temperature of water from the input file : " + str(water_temp))
print ("Printing the density of water from the input file : " +  str(water_density) + "\n")

input_file=open("density_air.dat",'r')
lines=input_file.readlines()

for x in lines:
	if x[0]=="#" or x[0]=="\n":
		continue
	else:
		data = x.strip().split("   ")
		air_temp.append(float(data[0]))
		air_density.append(float(data[1]))

print ("Printing the temperature of air from the input file : " + str(air_temp))
print ("Printing the density of air from the input file : " +  str(air_density) + "\n")


coeff1= polyfit(water_temp, water_density, 1)
coeff2=polyfit(water_temp, water_density, 2)
x= poly1d(coeff1)
y= poly1d(coeff2)
cord1= x(water_temp)
cord2= y(water_temp)
plot(water_temp, water_density, 'bo', water_temp, cord1, 'r--', water_temp, cord2, 'g--')
legend (["Data","Fitted degree 1 polynomial","Fitted degree 2 polynomial"])
title("Temperature dependence of water density")
xlabel("Temperature")
ylabel("Density")
axis([min(water_temp),max(water_temp),min(water_density),max(water_density)])
show(plot)

coeff1= polyfit(air_temp, air_density, 1)
coeff2=polyfit(air_temp, air_density, 2)
x= poly1d(coeff1)
y= poly1d(coeff2)
cord1= x(air_temp)
cord2= y(air_temp)
plot(air_temp, air_density, 'bo', air_temp, cord1, 'r--', air_temp, cord2, 'g--')
legend (["Data","Fitted degree 1 polynomial","Fitted degree 2 polynomial"])
title("Temperature dependence of air density")
xlabel("Temperature")
ylabel("Density")
axis([min(air_temp),max(air_temp),min(air_density),max(air_density)])
show(plot)


'''################################################################################
    End of Program
################################################################################'''
