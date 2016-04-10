# Author: Daniel Harper
# Assignment: Homework4 - P3.py
# Original Date: 03/23/2016
# Last Updated:  03/23/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
import matplotlib.pyplot as plt # plotting library
from numpy import * # arrays, linspaces, most math functions
#import operator # used in sorting dictionaries
import sys # take input from command line
import argparse # store input from command line

# Body Section#######################################################
#--------------------------------------------------------------------
# Work on the following problem. Name it as P3.py. You should be able
# to run it as:
# python P3.py 1 2.5 5
# which will generate 3 curves on the same figure. (Hint, use the 
# hold() function to plot multiple curves on the same figure)
#
# Make a program that reads a set of v0 values from the command line
# and plots the corresponding curves y(t)=v0t-0.5gt^2 in the same 
# figure (set g=9.81). Let t = [0,2v/g] for each curve, which implies
# that you need a different vector of t coordinates for each curve

# FUNCTION: heightFunction(v,lineType)-------------------------------
# Description: This function outputs a plot of an initial velocity. 
#	The formula the function is based on is:
#	h(t) = v*t - 0.5*g*t^2
#	t is the linspace of 100 points from 0 to 2*v/g
#	v is the input parameter (mentioned below)
#	g is constant at 9.81
# Input Parameters:
#	v : initial velocity to base the height of the graph
#	lineType: define the color and style of the graph's line
# Output : The plot of the height with the initial velocity of v
def heightFunction(v = 0, lineType = '-b'):
	t = linspace(0,2*v/9.81,100)
	y = []
	for x in t:
		y.append(v*x-(0.5)*(9.81)*x**2)
	return plt.plot(t,y,lineType, label="%d m/s"%(v))
#--------------------------------------------------------------------

try:
	B = [float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])]
	try:
		L = ['-r','-g','-b']
		i = 0
		hv = vectorize(heightFunction) # vectorize for efficiency
		for x in B:
			hv(x,L[i])
			i+= 1
		plt.xlabel("Time(seconds)")
		plt.ylabel("Height(meters)")
		plt.title("Projectile Motion")
		#plt.legend(["","b","","d","","f","g","h"])
		# plt.legend (["v0 = "+str(sys.argv[1])+" m/s","v1 = "+str(sys.argv[2])+" m/s","v2: = "+str(sys.argv[3])+" m/s"])
		plt.legend(loc='upper right', numpoints = 1,title='Initial Velocities')
		# numpoints = 1 is supposed to stop the legend duplicates, but it doesn't seem to work
		plt.show()
		
	except:
		print("CALCULATION ERROR: Something happened on my end")
except:
	print("INPUT ERROR: Numerical values only")
