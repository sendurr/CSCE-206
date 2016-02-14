# Author: Daniel Harper
# Assignment: Homework 1 - sin2_plus_cos2.py
# Original Date: 1/21/2016
# Last Updated:  1/21/2016
# Written using Python 3.4.3.7
# All rights reserved
# Description: Accomplish tasks outlined in the assignment document
#####################################################################
# Importation Section################################################
from math import * # basic math library

# Body Section#######################################################

# FUNCTION:trigIdentity(x)-------------------------------------------
# Description: Calculate sin(x)^2 + cos(x)^2 using the input x
# Input Parameters:
#	x : input variable for the calculation
def trigIdentity(x):
	val_1 = sin(x)**2 + cos(x)**2
	return(val_1)
#--------------------------------------------------------------------

inputValue = pi/4.0

print(trigIdentity(inputValue))

