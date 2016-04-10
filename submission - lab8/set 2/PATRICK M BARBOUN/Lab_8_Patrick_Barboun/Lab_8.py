import numpy as np 
import matplotlib.pyplot as py 

air_temp = list()
air_dens = list()
water_temp = list()
water_dens = list()

with open('density_air.dat','r') as fl:
	lines = fl.readlines()
	for i in lines:
		if i[0]=='#':
			lines.remove(i)
		else:
			x = i.strip().split()
			air_temp.append(float(x[0]))
			air_dens.append(float(x[1]))

with open('density_water.dat','r') as fl:
	lines = fl.readlines()
	for i in lines:
		if i[0]=='#':
			lines.remove(i)
		else:
			x = i.strip().split()
			water_temp.append(float(x[0]))
			water_dens.append(float(x[1]))

air_coeff1 = np.polyfit(air_temp,air_dens,1)
air_coeff2 = np.polyfit(air_temp,air_dens,2)
a = np.poly1d(air_coeff1)
c = np.poly1d(air_coeff2)
air_line_fit = a(air_temp)
air_quad_fit = c(air_temp)

water_coeff1 = np.polyfit(water_temp,water_dens,1)
water_coeff2 = np.polyfit(water_temp,water_dens,2)
b = np.poly1d(water_coeff1)
d = np.poly1d(water_coeff2)
water_line_fit = b(water_temp)
water_quad_fit = d(water_temp)

py.figure(1)
py.subplot(121)
py.plot(air_temp,air_dens,'o',label = 'Air Data')
py.plot(air_temp,air_line_fit,'b--',label = 'Linear Fit')
py.plot(air_temp,air_quad_fit,'r--',label = 'Quadratic Fit')
py.xlabel('Temperature')
py.ylabel('Density')
py.grid(True)
py.title('Air Density')
py.legend()

py.subplot(122)
py.plot(water_temp,water_dens,'ro',label = 'Water Data')
py.plot(water_temp,water_line_fit,'b--',label = 'Linear Fit')
py.plot(water_temp,water_quad_fit,'r--',label = 'Quadratic Fit')
py.xlabel('Temperature')
py.ylabel('Density')
py.grid(True)
py.legend()
py.title('Water Density')
py.show()





	


