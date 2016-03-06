# Author: Daniel Harper
# Assignment: Homework 2 - P2.py
# Original Date: 2/4/2016
# Last Updated:  2/4/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
import numpy as np

# Body Section#######################################################
#--------------------------------------------------------------------
# Write a program that prints a table with t values in the first 
# column and the corresponding y(t) = Vo*t - 0.5gt^2 values in the 
# second column. Use n uniformly spaced t values throughout the 
# interval [0,2Vo/g]. Set Vo = 1, g = 9.81, and n = 11.



# FUNCTION: distance(v0 = 0, n = 1)----------------------------------
# Description: Calculate the height a projectile will be at the 
# specific amount of time t given the inital velocity and the 
#	formula: y(t) = Vot *t - 0.5gt^2
# Input Parameters:
#	v0 : number representing the initial velocity of the object
#	n : integer number to depict the number of time to output
# output : no formal output, but a table of the heights at various 
#	times will be printed on the screen
def distance(v0 = 0, n = 1):
	g = 9.81 # acceleration due to gravity (on Earth)
	i = 0 # counter to be used with respect to n
	timeTable = list(np.linspace(0,2*v0/g,n))
	for i in timeTable:
		print("%.2f \t %.2f"%(i,(v0 * i - 0.5 * g * i**2)))
#--------------------------------------------------------------------

distance(1,11)
