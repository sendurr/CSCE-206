# Author: Daniel Harper
# Assignment: Homework 3 - P1.py
# Original Date: 2/18/2016
# Last Updated:  2/18/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys

# Body Section#######################################################
#--------------------------------------------------------------------
# An arbitrary triangle can be described by the coordinates of its 
# three verticies: (x1,y1), (x2, y2), (x3, y3), numbered in a 
# counterclockwise direction. The area of the triangle is given by 
# the formula: 
# 	A = (1/2) * |x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1|
# Write a function area(vertices) that returns the area of a triangle
# whose vertices are specified by the argument verticies which is a
# nested list of the vertex coordinates. For example, vertices can be
# [[0,0],[1,0],[0,2]] if the three corners of the triangle have 
# coordinates (0,0), (1,0), and (0,2). Test the area function on a 
# triangle with known area
# Test your function with the following statement:
# area([[0,0],[1,0],[0,2]])

# FUNCTION: area(x)--------------------------------------------------
# Description: Calculate the area of a triangle with the 3 verticies
# 	in a list format
# Input Parameters:
#	x : 2 dimensional list containing the 3 verticies in the 
#	following format: [[x1,y1],[x2,y2],[x3,y3]]
# Output : a float number containing the area of the entered triangle
def area(x):
	#      =       x2*y3      -      x3*y2      -      x1*y3      +      x3*y1      +      x1*y2      -      x2*y1  
	output = (x[1][0]*x[2][1])-(x[2][0]*x[1][1])-(x[0][0]*x[2][1])+(x[2][0]*x[0][1])+(x[0][0]*x[1][1])-(x[1][0]*x[0][1])
	if output < 0:
		output = output*(-1.0)
	return output*(0.5)
#--------------------------------------------------------------------

print(area([[0,0],[1,0],[0,2]]))