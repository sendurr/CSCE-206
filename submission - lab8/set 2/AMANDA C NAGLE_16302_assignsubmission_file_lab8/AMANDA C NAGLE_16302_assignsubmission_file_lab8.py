from numpy import *
from matplotlib.pyplot import *

file1=open("density_water.dat",'r')
file2=open("density_air.dat",'r')
lines1=file1.readlines()
lines2=file2.readlines()

water_temp=[]
water_density=[]
air_temp=[]
air_density=[]

for x in lines1:
	if x[0]=="#" or x[0]=='/n':
		continue
	else:
		a=x.strip()
		b=a.split(' ')
		try:
			water_temp.append(float(b[0]))
			water_density.append(float(b[-1]))
		except:
			continue

for x in lines2:
	if x[0]=="#" or x[0]=='/n':
		continue
	else:
		a=x.strip()
		b=a.split(' ')
		try:
			air_temp.append(float(b[0]))
			air_density.append(float(b[-1]))
		except:
			continue

coeff= polyfit(water_temp, water_density, 1)
coeff2=polyfit(water_temp, water_density, 2)
p= poly1d(coeff)
q= poly1d(coeff2)
print p
print q
y_fit= p(water_temp)
y_fit2= q(water_temp)
plot(water_temp, water_density, 'b*', water_temp, y_fit, 'r-', water_temp, y_fit2, 'g-')
legend= ('data','fitted polynomial of degree %d')
title("water temp v water density")
xlabel('Water Temp')
ylabel('Water Density')
axis([0,120,950,1010])
show(plot)

coeff3= polyfit(air_temp, air_density, 1)
coeff4=polyfit(air_temp, air_density, 2)
s= poly1d(coeff3)
t= poly1d(coeff4)
y_fit3= s(air_temp)
y_fit4= t(air_temp)
plot(air_temp, air_density, 'b*', air_temp, y_fit3, 'r-', air_temp, y_fit4, 'g-')
legend= ('data','fitted polynomial of degree %d')
title("air temp v air density")
xlabel('Air Temp')
ylabel('air Density')
axis([-12,32,1.15,1.37])
show(plot)


