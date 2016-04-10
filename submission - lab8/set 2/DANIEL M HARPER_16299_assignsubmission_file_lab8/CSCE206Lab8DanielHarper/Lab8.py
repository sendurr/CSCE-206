# Author: Daniel Harper
# Assignment: Lab 8.py
# Original Date: 3/18/2016
# Last Updated:  3/18/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
import matplotlib.pyplot as plt # plotting library
from numpy import * # arrays, linspaces, most math functions
#import operator # used in sorting dictionaries
#import sys # take input from command line
#import argparse # store input from command line

# Body Section#######################################################
#--------------------------------------------------------------------

inputFile = open("density_air.dat", 'r')
airLines = inputFile.readlines()
inputFile.close()

inputFile = open("density_water.dat", 'r')
waterLines = inputFile.readlines()
inputFile.close()

air_temp = []
air_density = []
water_temp = []
water_density = []

for x in airLines:
	line = x.strip().split("    ") # strip only does front and back of a string, not the body
	try:
		air_temp.append(float(line[0].strip()))
		air_density.append(float(line[1].strip()))
	except:
		continue

for x in waterLines:
	line = x.strip().split("   ") # strip only does front and back of a string, not the body
	try:
		water_temp.append(float(line[0].strip()))
		water_density.append(float(line[1].strip()))
	except:
		continue

air_coeff = polyfit(air_temp,air_density, 1)
ap = poly1d(air_coeff)
air_density_fit = ap(air_temp)

water_coeff = polyfit(water_temp,water_density,1)
wp = poly1d(water_coeff)
water_density_fit = wp(water_temp)

plt.plot(air_temp,air_density, 'ro', air_temp, air_density_fit, 'b-')
plt.title("Air Measurements")
plt.xlabel("Temperature(C)")
plt.ylabel("Density(Kg/m^3)")
plt.show()

plt.plot(water_temp,water_density, 'ro', water_temp, water_density_fit, 'b-')
plt.title("Water Measurements")
plt.xlabel("Temperature(C)")
plt.ylabel("Density(Kg/m^3)")
plt.show()

# print("air_temp:",len(air_temp))
# print("air_density:",len(air_density))
# print("air_density_fit:",len(air_density_fit))

# print("water_temp:",len(water_temp))
# print("water_density:",len(water_density))
# print("water_density_fit:",len(water_density_fit))
