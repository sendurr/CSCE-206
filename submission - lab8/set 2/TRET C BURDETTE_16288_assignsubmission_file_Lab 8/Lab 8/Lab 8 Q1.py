# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:01:51 2016

@author: Tret Burdette
"""

from numpy import*
import matplotlib.pyplot as plt

f1=open("density_water.dat",'r')
f2=open("density_air.dat",'r')
water_temp=[]
for line in f1:
	water_temp.append(float(line.strip()))
print water_temp
x=water_temp
water_density=[]
for line in f1:
	water_density.append(float(line.strip()))
print water_density 
y=water_density
air_temp=[]
for line in f2:
	air_temp.append(float(line.strip()))
x1=air_temp
air_density=[]
for line in f2:
	air_density.append(float(line.strip()))
y1=air_temp

coeff=polyfit(x,y,deg)
p=poly1d(coeff)
print p
y_fitted=p(x)
plot(x,y,'r-',x,y_fitted,'b-',
	legend=('data','fitted polynomial of degree%d' % deg))


coeff=polyfit(x,y,deg)
p=poly1d(coeff)
print p
y_fitted=p(x)
plot(x1,y1,'r-',x,y_fitted,'b-',
	legend=('data','fitted polynomial of degree%d' % deg))