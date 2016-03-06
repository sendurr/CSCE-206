# Author: Daniel Harper
# Assignment: Homework 2 - P3.py
# Original Date: 2/4/2016
# Last Updated:  2/8/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random

# Body Section#######################################################
#--------------------------------------------------------------------
# We want to generate x coordinates between 1 and 2 with spacing 
# 0.01. The coordinates are given by the formula Xi = 1 + ih, where 
# h = 0.01 and i runs over integers 0, 1,..., 100. Compute the Xi 
# values and store them in a list. Use a for loop, and append each 
# new Xi value to a list, which is empty initially.

myList = []
h = 0.01
i = 0
Xi = 1 
while i < 100:
	Xi = 1.0 + i*h
	myList.append(Xi)
	i += 1

print(myList)