import matplotlib.pyplot as plt
from math import *
import numpy as np

infile1=open('density_air.dat', 'r')
temp_air=[]
density_air=[]
for line in infile1:
    if line[0]=='#' or line.strip()=='':
        continue
    else:
        words=line.split()
        temp_air.append(float(words[0]))
        density_air.append(float(words[1]))
infile1.close()

infile2=open('density_water.dat', 'r')
temp_water=[]
density_water=[]
for line in infile2:
    if line[0]== '#' or line.strip()=='':
        continue
    else:
        words=line.split()
        temp_water.append(float(words[0]))
        density_water.append(float(words[1]))
infile2.close()

coeff1=np.polyfit(temp_air, density_air, 1)
p=np.poly1d(coeff1)
y_fitted1=p(temp_air)
coeff2=np.polyfit(temp_air, density_air, 2)
p=np.poly1d(coeff2)
y_fitted2=p(temp_air)

plt.plot(temp_air, density_air, 'bo', label='data')
plt.plot(temp_air, y_fitted1, 'r--', label='1 degree')
plt.plot(temp_air, y_fitted2, 'g--', label='2 degree')
plt.xlabel('Temperature(deg C)')
plt.ylabel('Density (kg/m^3)')
plt.title('Temperature Dependence of Air Density')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()

coeff1=np.polyfit(temp_water, density_water, 1)
p=np.poly1d(coeff1)
y_fitted1=p(temp_water)
coeff2=np.polyfit(temp_water, density_water, 2)
p=np.poly1d(coeff2)
y_fitted2=p(temp_water)

plt.plot(temp_water, density_water, 'bo', label='data')
plt.plot(temp_water, y_fitted1, 'r--', label='1 degree')
plt.plot(temp_water, y_fitted2, 'g--', label='2 degree')
plt.xlabel('Temperature (deg C)')
plt.ylabel('Density (kg/m^3)')
plt.title('Temperature Dependence of Water Density')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()