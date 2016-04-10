from numpy import *
import matplotlib.pyplot as plt
infile=open("density_water.dat",'r')
infile2=open("density_air.dat",'r')

lines=infile.readlines()
lines2=infile2.readlines()

water_temp=[]
water_density=[]
airtemp=[]
airdensity=[]

for x in lines:
	if x[0]=="#":
		continue
	else:
		items=x.strip()
		items2=items.split(' ')
		try:
			water_temp.append(float(items2[0]))
			water_density.append(float(items2[-1]))
		except:
			continue
#print (water_temp)
#print (water_density)

for x in lines2:
	if x[0]=="#":
		continue
	else:
		items=x.strip()
		items2=items.split(' ')
		try:
			airtemp.append(float(items2[0]))
			airdensity.append(float(items2[-1]))
		except:
			continue
#print (airtemp)
#print (airdensity)

coeff=polyfit(water_temp, water_density,1)
p=poly1d(coeff)
print (p)
y_fitted=p(water_temp)
plt.plot(water_temp,water_density,'r-',water_temp,y_fitted,'bo')
plt.legend(['data','fitted polynomial of degree 1','fitted polynomial of degree 2'])

plt.plot(water_temp,water_density)
plt.title("Temperature dependence of water density")
plt.xlabel('Water Temp')
plt.ylabel('Water Density')
plt.axis([0,105,960,1005])
plt.show()


coeff2=polyfit(airtemp, airdensity,1)
p2=poly1d(coeff2)
print (p2)
y_fitted2=p2(airtemp)
plt.plot(airtemp,airdensity,'r-',airtemp,y_fitted2,'bo')
plt.legend=(['data','fitted polynomial of degree %d'])

plt.plot(airtemp,airdensity)
plt.title("Temperature dependence of air density")
plt.xlabel('Air Temp')
plt.ylabel('Air Density')
plt.axis([-10,32,1.15,1.40])
plt.show()