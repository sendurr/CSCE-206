# Author: Daniel Harper
# Assignment: Homework 1 - Gaussian_function1.py
# Original Date: 1/21/2016
# Last Updated:  1/21/2016
# Written using Python 3.4.3.7
# All rights reserved
# Description: Accomplish tasks outlined in the assignment document
#####################################################################
# Importation Section################################################
from math import * # basic math library

# Body Section#######################################################

# FUNCTION:gaussian1(m,s,x)------------------------------------------
# Description: Calculate the bell-shaped Gaussian function
# Input Parameters:
#	m : input variable (unsure actual meaning in the calculation)
#	s : input variable (unsure actual meaning in the calculation)
#	x : input variable (unsure actual meaning in the calculation)
def gaussian1(m,s,x):
	output = ((1.0/(sqrt(2.0*pi)*s))*exp((-(1.0/2.0))*((x-m)/x)**2))
	return output
#--------------------------------------------------------------------

a = 0.0
b = 2.0
c = 1.0

print(gaussian1(a,b,c))

#HAND CALCULATIONS---------------------------------------------------
# base function
# f(x) = (1.0 / (sqrt(2.0*pi)*s)) * exp((-(1.0/2.0)) * ((x-m)/x)**2)
#
# convert for hand work
# f(x) = (1/(s*sqrt(2pi)))*exp((-(1/2))*((x-m)/x)^2)
#
# substitute m and s for setup
# f(x) = (1/(2sqrt(2pi)))*exp((-(1/2))*((x-0)/x)^2)
#
# set x = 1
# f(x) = (1/(2sqrt(2pi)))*exp((-(1/2))*((1-0)/1)^2)
#
# solve
# f(x) = 1/(2sqrt(2pi))*exp((-(1/2))*((1-0)/1)^2)
# f(x) = 1/(2sqrt(2pi))*exp((-(1/2))*(1/1)^2)
# f(x) = 1/(2sqrt(2pi))*exp((-.5*(1)^2)
# f(x) = 1/(2sqrt(2pi))*exp(-.5*1)
# f(x) = 1/(2sqrt(2pi))*exp(-.5)
# 
# plug into calculator
# 0.1209853623
