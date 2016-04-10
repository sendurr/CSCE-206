Water_temp=[]
water_density=[]
Air_temp=[]
air_density=[]

water = open('density_water.dat','r')
lines = water.readlines()
for x in lines:
	if x[0]=="#" or x[0]=="\n":
		continue
	#data = x.strip().split(",")
	#data_number = []
	#for x in data:
		#if data is number:

	#if data[0].isdigit():
	else:
		data = x.strip().split("   ")
		Water_temp.append(float(data[0]))
		water_density.append(float(data[1]))
			#x.append(data_number)
			#Water_temp(0)=data_number(0)
	#for x in data_number:
		#if x%2==0:
			#x.append(Water_temp)
		#else:
			#x.append(water_density)

print Water_temp
print water_density

# air = open('density_air.dat','r')
# lines = air.readlines()
# for x in lines:
# 	data = x.strip().split(",")
# 	data_number = []
# 	for x in data:
# 		if data is number:
# 			x.append(data_number)
# 	Air_temp(0)=data_number(0)
# 	for x in data_number:
# 		if x%2==0:
# 			x.append(Air_temp)
# 		else:
# 			x.append(air_density)

# import math
# import numpy
# import pylab
# import matplotlib.pyplot as plt

from numpy import *
from matplotlib.pyplot import *

#coeff1 = polyfit(Water_temp,water_density,deg)
coeff1 = polyfit(Water_temp,water_density,1)
p1 = poly1d(coeff1)
print(p1)
y_fitted1 = p1(x)

# coeff2 = polyfit(Air_temp,air_density,deg)
# p2 = poly1d(coeff)
# print(p2)
# y_fitted2 = p2(x)



pylab.plot(Water_temp,water_density,'r-',Water_temp,y_fitted1,'b-',
	legend=('data','fitted polynomial of %d'%d))
# plt.plot(Water_temp,water_density,'r-',Water_temp,y_fitted1,'b-',
# 	legend=('data','fitted polynomial of %d'%d))
plt.show()